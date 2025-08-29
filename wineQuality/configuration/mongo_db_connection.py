import os 
import sys 

from wineQuality.constants import DATABASE_URL , DATABASE_NAME
from wineQuality.logger import logging
from wineQuality.exception import WineException

import pymongo 
import certifi

ca = certifi.where()


# class which will give us access to the mongoDb database
class MongoDbConnection:
    client = None 
    
    def __init__(self , database_name: str = DATABASE_NAME):
        try:
            # make a new connection if connection not exists 
            if MongoDbConnection.client is None:
                # make the connection 
                mongoDbUrl = DATABASE_URL
                
                if mongoDbUrl is None:
                    logging.info("Missing mongo_db_url in the .env file")
                    raise WineException(e , sys) 
                
                # connection string available make the connection
                MongoDbConnection.client = pymongo.MongoClient(mongoDbUrl , tlsCAFile = ca) 
            
            # set the database and client
            self.client = MongoDbConnection.client
            self.database_name = database_name
            # get the database
            self.database = self.client[self.database_name]
            
            logging.info("MongoDB connection successfull")
            
        except Exception as e:
            raise WineException(e , sys)  