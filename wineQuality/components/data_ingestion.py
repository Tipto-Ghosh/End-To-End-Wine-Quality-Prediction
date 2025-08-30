import sys 
import warnings
warnings.filterwarnings("ignore")
from pandas import DataFrame
from sklearn.model_selection import train_test_split

from wineQuality.logger import logging
from wineQuality.exception import WineException

from wineQuality.data_access import WineData
from wineQuality.entity.config_entity import DataIngestionConfig
from wineQuality.entity.artifact_entity import DataIngestionArtifact
from wineQuality.utils.main_utils import save_csv_file


class DataIngestion:
   
    def __init__(self , data_ingestion_config: DataIngestionConfig = DataIngestionConfig()):
        """This class is responsible to get data from database and save raw data inside feature store.
           Do train and test split, save both train and test data.

        Args:
            data_ingestion_config (DataIngestionConfig, optional): Defaults to DataIngestionConfig().
        """
        
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise WineException(e , sys)   
    
    
    def export_data_into_feature_store(self) -> DataFrame:
        """Reads the data fram mongoDb and saves the raw data inside feature_store

        Returns:
            DataFrame: raw data dataframe
        """
        try:
            logging.info("Entered into export_data_into_feature_store of class DataIngestion") 
            logging.info(f"Getting data from mongodb collection: {self.data_ingestion_config.collection_name}")
            
            # read the data from database
            wine_data_obj = WineData()
            dataframe = wine_data_obj.get_data_from_database_as_dataframe(
                collection_name = self.data_ingestion_config.collection_name
            )
            
            logging.info("Data conversion from Collection to DataFrame successful")
            logging.info(f"Shape of the dataframe: {dataframe.shape}")
            
            # save data inside feature store
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            save_csv_file(feature_store_file_path , dataframe)
            
            return dataframe
        
        except Exception as e:
            raise WineException(e , sys)   
    
    
    def split_data_as_train_test(self , dataframe: DataFrame) -> None:
        """Take the raw dataframe and do train and test split. Save both train and test set as csv.
        Args:
            dataframe (DataFrame): raw data dataframe
        """
        logging.info("Entered split_data_as_train_test method of data_ingestion")
        
        try:
            # do the split
            train_set , test_set = train_test_split(
                dataframe , test_size = self.data_ingestion_config.train_test_split_ratio , random_state = 42 
            )
            
            #  save the train and test data
            save_csv_file(
                file_path = self.data_ingestion_config.train_data_file_path,
                data = train_set
            )
            save_csv_file(
                file_path = self.data_ingestion_config.test_data_file_path,
                data = test_set
            )
            logging.info("Saved train and test data as csv file")
            
        except Exception as e:
            raise WineException(e , sys)   
    
    
    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        """This method initiates the data ingestion components of training pipeline.
           Merge to method export_data_into_feature_store and split_data_as_train_test.
           
        Returns:
            DataIngestionArtifact: _description_
        """
        
        logging.info("Entered initiate_data_ingestion method of Data_Ingestion class")
        
        try:
            # 1. get the raw dataframe
            raw_dataframe =  self.export_data_into_feature_store()
            logging.info("from initiate_data_ingestion: Got the data from mongodb as Dataframe")
            
            # 2. do the train test split
            self.split_data_as_train_test(dataframe = raw_dataframe)
            logging.info("Performed train test split on the dataset")
            
            # 3. make the data ingestion artifacts
            data_ingestion_artifact = DataIngestionArtifact(
                train_data_file_path = self.data_ingestion_config.train_data_file_path,
                test_data_file_path = self.data_ingestion_config.test_data_file_path
            )
            
            logging.info(f"Data ingestion artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact
        except Exception as e:
            raise WineException(e , sys)   