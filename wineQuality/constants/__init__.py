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

# Data validation Constants
DATA_VALIDATION_DIR_NAME : str = "data_validation"
DATA_VALIDATION_DRIFT_REPORT_DIR : str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME : str = "report.yaml"


# Data Transformation Constants
DATA_TRANSFORMATION_DIR_NAME : str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR : str = "transformed_data"
DATA_TRANSFORMATION_PREPROCESSOR_OBJECT_DIR : str = "transformed_object"


# Model Trainer realted contant start with MODEL_TRAINER
MODEL_TRAINER_DIR_NAME : str = "model_trainer"
# trained model path
MODEL_TRAINER_TRAINED_MODEL_DIR : str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME : str = "recent_trained_model.pkl"
# Path to model.yaml
MODEL_TRAINER_MODEL_CONFIG_FILE_PATH : str = os.path.join("config" , "params.yaml")
MODEL_TRAINER_EXPECTED_SCORE : float = 0.75 # minimal accuracy score for classification

# Reports directory for tuned models
MODEL_TRAINER_ALL_MODEL_REPORT_DIR: str = "all_model_report"
# File path where all tuned models' details will be saved
MODEL_TRAINER_ALL_TUNED_MODEL_REPORT_FILE_PATH: str = "all_tuned_model_report.yaml" 


# Model Evaluation related constants
PRODUCTION_MODEL_PATH : str = os.path.join("production" , MODEL_FILE_NAME)
PRODUCTION_PREPROCESSOR_PATH : str = os.path.join("production" , PREPROCESSOR_OBJECT_FILE_NAME)
