import os , sys 
import pandas as pd 
import numpy as np 
from typing import Optional

from wineQuality.logger import logging
from wineQuality.exception import WineException
from wineQuality.configuration.mongo_db_connection import MongoDbConnection 

class WineData:
    """
    This class is responsible to read the from the database collection.
    Also make the dataframe and replace "na" with NaN and also remove extra _id column that Mongo Creates.
    """
    def __init__(self):
        # make the connection with database
        try:
            self.mongo_connection =  MongoDbConnection()
        except Exception as e:
            raise WineException(e , sys) 
    
    def get_data_from_database_as_dataframe(self , collection_name: str , database_name: Optional[str] = None) -> pd.DataFrame:
        """_summary_

        Args:
            collection_name (str): Name of the database collection
            database_name (Optional[str], optional): mongo database name. Defaults to None.

        Returns:
            pd.DataFrame: returns the raw data as dataframe
        """
        
        try:
            # check database if given or not
            if database_name is None:
                # then set database name from client
                database = self.mongo_connection.database
            else:
                database = self.mongo_connection.client[database_name]
            
            # get the collection
            collection_obj = database[collection_name]
            data_list = list(collection_obj.find())
            
            # convert the list into a dataframe
            dataframe = pd.DataFrame(data_list)
            
            # remove extra _id column that mongo makes
            if "_id" in dataframe.columns:
                dataframe.drop(columns = ["_id"] , axis = 1 , inplace = True)
            
            # replace the "na" with NaN
            dataframe.replace({"na" : np.nan} , inplace = True)
            
            return dataframe 
        except Exception as e:
            raise WineException(e , sys)