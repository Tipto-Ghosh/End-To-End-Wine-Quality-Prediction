import os 
import sys 
import json
import warnings
warnings.filterwarnings("ignore")
from pandas import DataFrame
from evidently.model_profile import Profile
from evidently.profile_sections import  DataDriftProfileSection

from wineQuality.logger import logging
from wineQuality.exception import WineException

from wineQuality.utils.main_utils import read_yaml_file , write_yaml_file , read_csv
from wineQuality.entity.config_entity import DataValidationConfig
from wineQuality.entity.artifact_entity import DataIngestionArtifact , DataValidationArtifact
from wineQuality.constants import SCHEMA_FILE_PATH


class DataValidation:
    def __init__(self , data_ingestion_artifact : DataIngestionArtifact , data_validation_config : DataValidationConfig = DataValidationConfig()):
        """This class is responsible to do data validation.

        Args:
            data_ingestion_artifact (DataIngestionArtifact): object of DataIngestionArtifact
            data_validation_config (DataValidationConfig, optional): _description_. Defaults to DataValidationConfig().
        """
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
            
            # read SCHEMA.yaml
            logging.info("reading the schema file from DataValidation")
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)
            logging.info("reading the schema file from DataValidation is done")
        except Exception as e:
            raise WineException(e , sys)
    
    
    def validate_numerical_columns(self , dataframe : DataFrame) -> bool:
        """Validate all the numerical feature exists or not.

        Args:
            dataframe (DataFrame): pass dataframe for which we want to check

        Returns:
            bool: if all numerical columns exists then return True otherwise False
        """
        # get all the columns from the dataframe
        dataframe_columns = dataframe.columns.to_list()
        
        # get all the numerical columns from the schema file
        schema_numerical_columns = self._schema_config['numerical_columns']
        
        # now check all the numerical columns are present or not
        missing_numerical_columns = []
        
        for column  in schema_numerical_columns:
            if column not in dataframe_columns:
                missing_numerical_columns.append(column)
        
        if len(missing_numerical_columns) > 0:
            logging.info(f"Missing Numerical Column: {missing_numerical_columns}")
        
        return False if len(missing_numerical_columns) > 0 else True
    
    def validate_categorical_columns(self , dataframe : DataFrame) -> bool:
        """Validate all the categorical feature exists or not.

        Args:
            dataframe (DataFrame): pass dataframe for which we want to check

        Returns:
            bool: if all categorical columns exists then return True otherwise False
        """
        # get all the columns from the dataframe
        dataframe_columns = dataframe.columns.to_list()
        
        # get all the categorical columns from the schema file
        schema_categorical_columns = self._schema_config['categorical_columns']
        
        # now check all the categorical columns are present or not
        missing_categorical_columns = []
        
        for column in schema_categorical_columns:
            if column not in dataframe_columns:
                missing_categorical_columns.append(column)
        
        if len(missing_categorical_columns) > 0:
            logging.info(f"Missing categorical Column: {missing_categorical_columns}")
        
        return False if len(missing_categorical_columns) > 0 else True
    
    
    def initiate_column_validation(self , dataframe : DataFrame) -> bool:
        """Check all the numerical and categorical exists or not

        Args:
            dataframe (DataFrame): pass dataframe for which we want to check

        Returns:
            bool: if all numerical and categorical columns exists then return True otherwise False
        """
        
        try:
            logging.info("Entered into initiate_column_validation")
            
            numerical_column_check = self.validate_numerical_columns(dataframe)
            categorical_column_check = self.validate_categorical_columns(dataframe)
            
            status = numerical_column_check and categorical_column_check
            logging.info(f"Column validation status is [{status}]")
            
            return status
        except Exception as e:
            raise WineException(e , sys)
    
    
    # do the data drift check
    def detect_data_drift(self , reference_df: DataFrame , current_df: DataFrame) -> bool: 
        """Check Train and Test Dataset has data drift or not

        Args:
            reference_df (DataFrame): Train dataset
            current_df (DataFrame): Test dataset

        Returns:
            bool: returns False if not data drift otherwise return False
        """
        try:
            # create the profile
            data_drift_profile = Profile(sections = [DataDriftProfileSection()]) 
            data_drift_profile.calculate(reference_data = reference_df , current_data = current_df)
            
            # make the report as json
            report = data_drift_profile.json()
            json_report = json.loads(report)
            
            logging.info("Saving the data drift report as yaml file")
            write_yaml_file(
                file_path = self.data_validation_config.data_drift_file_path,
                content = json_report
            )
            logging.info("Saved the data drift report as yaml file")
            
            n_features = json_report["data_drift"]["data"]["metrics"]["n_features"]
            n_drifted_features = json_report["data_drift"]["data"]["metrics"]["n_drifted_features"]
            data_drift_percentage = (n_drifted_features / n_features) * 100
            logging.info(f"Out of {n_features} columns data drift detected in {n_drifted_features} columns")
            logging.info(f"Data Drift percentage: {data_drift_percentage} %")
            drift_status = json_report["data_drift"]["data"]["metrics"]["dataset_drift"]
            
            # drift_status == False if no data drift -> everthing is okay
            # drift_status == True -> Data Drift detected 
            return drift_status
        
        except Exception as e:
            raise WineException(e , sys)
    
    def initiage_data_validation(self) -> DataValidationArtifact:
        """This method is responsible to do the whole data validation part and make the data validation artifact.

        Returns:
            DataValidationArtifact: Object of DataValidationArtifact
        """
        try:
            logging.info("Starting data validation")
            
            # get the train and test dataset
            train_df = read_csv(self.data_ingestion_artifact.train_data_file_path)
            test_df = read_csv(self.data_ingestion_artifact.test_data_file_path)
            
            logging.info(f"train_df data shape: {train_df.shape}")
            logging.info(f"test_df data shape: {test_df.shape}")
            
            # check column validity
            train_data_column_validity = self.initiate_column_validation(train_df)
            
            if train_data_column_validity == False:
                raise Exception("Train data column validation failed")
            
            test_data_column_validity = self.initiate_column_validation(test_df)
            
            if test_data_column_validity == False:
                raise Exception("Train data column validation failed")
            
            # train and test data column validation status
            column_validation_status = train_data_column_validity and test_data_column_validity
            
            data_validation_status = False
            
            # if column_validation_status is OK then start data drift
            if column_validation_status:
                drift_status = self.detect_data_drift(reference_df = train_df , current_df = test_df)
            
                # if data drift detected
                if drift_status:
                    logging.info("Data Drift Detected")
                    data_validation_status = False
                else:
                    logging.info("Data Drift Not Detected")
                    data_validation_status = True
            else:
                data_validation_status = False 
            
            # now make the artifact for data validation
            data_validation_artifact = DataValidationArtifact(
                train_data_file_path = self.data_ingestion_artifact.train_data_file_path,
                test_data_file_path = self.data_ingestion_artifact.test_data_file_path,
                data_validation_status = data_validation_status,
                data_drift_report_file_path = self.data_validation_config.data_drift_file_path
            )
            logging.info(f"Data validation artifact created with validation status: [{data_validation_status}]")
            return data_validation_artifact
        
        except Exception as e:
            raise WineException(e , sys)