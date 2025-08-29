import os 
from wineQuality.constants import *
from datetime import datetime
from dataclasses import dataclass


TIMESTAMP : str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")


@dataclass
class TrainingPipelineConfig:
    pipeline_name : str = PIPELINE_NAME
    artifact_dir : str = os.path.join(ARTIFACT_DIR , TIMESTAMP)
    timestamp = TIMESTAMP

training_pipeline_config : TrainingPipelineConfig = TrainingPipelineConfig()

@dataclass
class DataIngestionConfig:
    # artifact/timestamp/data_ingestion
    data_ingestion_dir : str = os.path.join(training_pipeline_config.artifact_dir , DATA_INGESTION_DIR_NAME)
    # artifact/timestamp/data_ingestion/feature_store/wine.csv
    feature_store_file_path : str = os.path.join(data_ingestion_dir , DATA_INGESTION_FEATURE_STORE_DIR , RAW_DATA_FILE_NAME)
    # artifact/timestamp/data_ingestion/ingested/train.csv
    train_data_file_path : str = os.path.join(data_ingestion_dir , DATA_INGESTION_INGESTED_DIR , TRAIN_FILE_NAME)
    # artifact/timestamp/data_ingestion/ingested/test.csv
    test_data_file_path : str = os.path.join(data_ingestion_dir , DATA_INGESTION_INGESTED_DIR , TEST_FILE_NAME)
    train_test_split_ratio : float = DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
    collection_name : str = COLLECTION_NAME


@dataclass
class DataValidationConfig:
    # artifact/timestamp/data_validation/
    data_validation_dir : str = os.path.join(training_pipeline_config.artifact_dir , DATA_VALIDATION_DIR_NAME)
    # artifact/timestamp/data_validation/drift_report/report.yaml
    data_drift_file_path : str = os.path.join(data_validation_dir , DATA_VALIDATION_DRIFT_REPORT_DIR , DATA_VALIDATION_DRIFT_REPORT_FILE_NAME)