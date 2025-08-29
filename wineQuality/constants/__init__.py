import os 
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


# database related constants
DATABASE_URL = os.getenv("DATABASE_URL") # load from .env file
DATABASE_NAME = "wineData"
COLLECTION_NAME = "wineCollection"


# Raw data file name[feature store]
RAW_DATA_FILE_NAME : str = "wine.csv"

# Pipeline Name
PIPELINE_NAME : str = "wineQuality"


ARTIFACT_DIR : str = "artifacts"

TRAIN_FILE_NAME : str = "train.csv"
TEST_FILE_NAME : str = "test.csv"


PREPROCESSOR_OBJECT_FILE_NAME = "preprocessor.pkl"
MODEL_FILE_NAME = "model.pkl"


TARGET_COLUMN = "quality"
SCHEMA_FILE_PATH = os.path.join("config" , "schema.yaml")



# Data Ingestion Constants
DATA_INGESTION_COLLECTION_NAME : str = COLLECTION_NAME
DATA_INGESTION_DIR_NAME : str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR : str = "feature_store"
DATA_INGESTION_INGESTED_DIR : str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO : str = 0.2 # test size