import sys 
import os 
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import pandas as pd 
from sklearn.preprocessing import FunctionTransformer , StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from imblearn.combine import SMOTEENN

from wineQuality.constants import SCHEMA_FILE_PATH , TARGET_COLUMN
from wineQuality.logger import logging
from wineQuality.exception import WineException

from wineQuality.entity.config_entity import DataTransformationConfig , DataValidationConfig
from wineQuality.entity.artifact_entity import DataTransformationArtifact , DataValidationArtifact

from wineQuality.utils.main_utils import save_object , save_numpy_array_data , read_csv , read_yaml_file , drop_columns
from wineQuality.entity.estimator import TargetValueMapping
from collections import Counter



class DataTransformation:
    def __init__(self , data_transformation_config: DataTransformationConfig , data_validation_artifact: DataValidationArtifact):
        """This class is responsible for doing all the preprocessing task.

        Args:
            data_transformation_config (DataTransformationConfig): _description_
            data_validation_artifact (DataValidationArtifact): _description_
        """
        try:
            self.data_transformation_config = data_transformation_config
            self.data_validation_artifact = data_validation_artifact
            
            # read the schema file cause we need to know the drop and transformation column names
            self._schema_config = read_yaml_file(file_path = SCHEMA_FILE_PATH)
        except Exception as e:
            raise WineException(e , sys)
    
    
    def get_data_transformation_object(self) -> Pipeline:
        """ 
        This method creates and returns a data transformer(preprocessor) object for the data
        """
        
        try:
            logging.info("Entered get_data_transformer_object method of DataTransformation class")
            
            # make the transformation pipeline
            
            # get the columns where we need to do transformations
            log_cols = self._schema_config["log_transformation"]
            logging.info(f"Got log_cols: {log_cols}")
            sqrt_cols = self._schema_config["sqrt_transformation"]
            logging.info(f"Got sqrt_cols: {sqrt_cols}")
            other_cols = self._schema_config["other_columns"]
            logging.info(f"Got other_cols: {other_cols}")
            
            
            # define log transformers  
            log_pipeline = Pipeline(steps = [
                ("log" , FunctionTransformer(np.log1p , validate = False)) , 
                ("scaler" , StandardScaler())
            ])
            
            # define sqrt transformer with scaling 
            sqrt_pipeline = Pipeline(steps = [
                ("sqrt" , FunctionTransformer(np.sqrt , validate = False)), 
                ("scaler" , StandardScaler())
            ])
            
            # define a scaler for others column
            scaler_pipeline = Pipeline(steps = [
                ("scaler" , StandardScaler())
            ])
            
            # define the column transformer 
            preprocessor = ColumnTransformer(
                transformers = [
                    ("log" , log_pipeline , log_cols),
                    ("sqrt" , sqrt_pipeline , sqrt_cols),
                    ("others" , scaler_pipeline , other_cols)
                ]
            )
            
            logging.info("Created the preprocessor object from get_data_transformation_object")
            return preprocessor
        except Exception as e:
            raise WineException(e , sys)
    
    
    # do the data cleaning things
    def get_cleaned_data(self , dataframe: pd.DataFrame) -> pd.DataFrame:
        """This method do all the data cleaning like dropping unwanted columns , removing outliers and so on.

        Args:
            dataframe (pd.DataFrame): _description_

        Returns:
            pd.DataFrame: cleaned data. ready to pass in preprocessing.
        """
        
        # First drop all the unwanted collumns
        drop_cols = self._schema_config["drop_columns"]
        df = drop_columns(df = dataframe , cols = drop_cols)
        
        # column citric acid values with greater than 0.95 is outlier remove all where value crosses the thresold 
        logging.info("Doing => df = df[df['citric acid'] <= 0.95]")
        df = df[df['citric acid'] <= 0.95]
        
        # residual sugar column has outlier, remove all rows where values are greater than 25
        logging.info("Doing => df = df[df['residual sugar'] <= 25]")
        df = df[df['residual sugar'] <= 25]
        
        # total sulfur dioxide has outlier 
        logging.info("Doing => df = df[df['total sulfur dioxide'] <= 280]")
        df = df[df['total sulfur dioxide'] <= 280]
        logging.info("Data cleaning done")
        return df 
    
    
    def initiate_data_transformation(self , ) -> DataTransformationArtifact:
        """ 
        This method initiates the data transformation component for the pipeline
        """
        
        try:
            logging.info("Entered initiate_data_transformation method")
            
            # check data validation status
            if self.data_validation_artifact.data_validation_status == True:
                logging.info("Starting data transformation")
                
                # get the train and test dataframe
                train_df = read_csv(self.data_validation_artifact.train_data_file_path)
                test_df = read_csv(self.data_validation_artifact.test_data_file_path)
                
                # convert quality to classification value
                mapper = TargetValueMapping()
                train_df[TARGET_COLUMN] = train_df[TARGET_COLUMN].apply(mapper.wine_label)
                logging.info(f"for train_df quality is converted into: [{train_df[TARGET_COLUMN].unique()}]")
                
                test_df[TARGET_COLUMN] = test_df[TARGET_COLUMN].apply(mapper.wine_label)
                logging.info(f"for test_df quality is converted into: [{test_df[TARGET_COLUMN].unique()}]") 
                
                
                logging.info(f"from initiate_data_transformation method: train_df shape before cleaning [{train_df.shape}]")
                logging.info(f"from initiate_data_transformation method: test_df shape before cleaning[{test_df.shape}]")
                
                # do the data cleaning part
                logging.info("Data cleaning part started for train_df")
                train_df = self.get_cleaned_data(train_df)
                logging.info("Data Cleaning done for train_df")
                
                logging.info("Data cleaning part started for test_df")
                test_df = self.get_cleaned_data(test_df)
                logging.info("Data Cleaning done for test_df")
                
                logging.info(f"from initiate_data_transformation method: train_df shape before cleaning [{train_df.shape}]")
                logging.info(f"from initiate_data_transformation method: test_df shape before cleaning[{test_df.shape}]")
                
                
                # separete target columns and input features[X , y]
                input_feature_train_df = train_df.drop(columns = [TARGET_COLUMN] , axis = 1)
                target_feature_train_df = train_df[TARGET_COLUMN]  
                logging.info("Separeting X and y from train dataframe")
                
                # separete target columns and input features[X , y] from test data
                input_feature_test_df = test_df.drop(columns = [TARGET_COLUMN] , axis = 1)
                target_feature_test_df = test_df[TARGET_COLUMN]
                logging.info("Separeting X and y from test dataframe")
                
                
                # get the preprocessor object
                preprocessor = self.get_data_transformation_object()
                logging.info("Got the preprocessor object")
                
                
                
                # do the fit_transform on train data
                logging.info("Applying preprocessing object on training dataframe and testing dataframe")
                
                input_feature_train_arr = preprocessor.fit_transform(input_feature_train_df)
                logging.info("Used the preprocessor object to fit transform the train features")
                
                # do the transformation on test data
                input_feature_test_arr = preprocessor.transform(input_feature_test_df)
                logging.info("Used the preprocessor object to transform the test features")
                
                # Handle imbalance problem
                logging.info("Applying SMOTEENN on Training dataset")
                # Resampling the minority class. The strategy can be changed as required. 
                smt = SMOTEENN(random_state = 42 , sampling_strategy = "minority")
                
                input_feature_train_final, target_feature_train_final = smt.fit_resample(
                    input_feature_train_arr , target_feature_train_df
                )
                logging.info("Applied SMOTEENN on training dataset")
                
                logging.info(f"After solving imbalance issue: y count in train data: {Counter(target_feature_train_df)}")
            
                logging.info("Created train array and test array")
                    
                logging.info("concatenating input_feature_train_final arr and target_feature_train_final arr")
                train_arr = np.c_[
                    input_feature_train_final, np.array(target_feature_train_final)
                ]
                
                logging.info("concatenating input_feature_test_final arr and target_feature_test_final arr")
                test_arr = np.c_[
                    input_feature_test_arr, np.array(target_feature_test_df)
                ]
                
                logging.info(f"Shape of train_arr: [{train_arr.shape}]")
                logging.info(f"Shape of test_arr: [{test_arr.shape}]")
                
                # save the preprocessor object
                save_object(
                    file_path = self.data_transformation_config.transformed_object_file_path,
                    obj = preprocessor
                )
                logging.info("saved preprocessor object")
                
                
                # save the train and test data as numpy array
                save_numpy_array_data(
                    file_path = self.data_transformation_config.transformed_train_data_file_path,
                    array = train_arr
                )
                logging.info("saved train arr")
                save_numpy_array_data(
                    file_path = self.data_transformation_config.transformed_test_data_file_path,
                    array = test_arr
                )
                logging.info("saved test arr")
                
                # make the data transformation artifact
                data_transformation_artifact = DataTransformationArtifact(
                    transformed_object_file_path = self.data_transformation_config.transformed_object_file_path,
                    transformed_train_data_file_path = self.data_transformation_config.transformed_train_data_file_path,
                    transformed_test_data_file_path = self.data_transformation_config.transformed_test_data_file_path
                )
                logging.info("Exited initiate_data_transformation method of Data_Transformation class")
                
                return data_transformation_artifact
            else:
                logging.info("data transformation failed because of validation status")
                raise Exception("data transformation failed because of validation status")
                
        except Exception as e:
            raise WineException(e , sys)