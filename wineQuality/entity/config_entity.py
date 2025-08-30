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



@dataclass
class DataTransformationConfig:
    # artifact/timestamp/data_transformation/
    data_transformation_dir : str = os.path.join(training_pipeline_config.artifact_dir , DATA_TRANSFORMATION_DIR_NAME)
    # artifact/timestamp/data_transformation/transformed_data/train.npy
    transformed_train_data_file_path : str = os.path.join(
        data_transformation_dir , DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR , 
        TRAIN_FILE_NAME.replace("csv" , "npy")
    )
    # artifact/timestamp/data_transformation/transformed_data/test.npy
    transformed_test_data_file_path : str = os.path.join(
        data_transformation_dir , DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR , 
        TEST_FILE_NAME.replace("csv" , "npy")
    )
    # artifact/timestamp/data_transformation/transformed_object/preprocessor.pkl
    transformed_object_file_path : str = os.path.join(
        data_transformation_dir , DATA_TRANSFORMATION_PREPROCESSOR_OBJECT_DIR , PREPROCESSOR_OBJECT_FILE_NAME 
    )


@dataclass
class ModelTrainerConfig:
    # artifact/timestamp/model_trainer
    model_trainer_dir : str = os.path.join(training_pipeline_config.artifact_dir , MODEL_TRAINER_DIR_NAME)
    # artifact/timestamp/model_trainer/trained_model/model.pkl
    trained_model_file_path : str = os.path.join(
        model_trainer_dir , MODEL_TRAINER_TRAINED_MODEL_DIR , MODEL_TRAINER_TRAINED_MODEL_NAME
    )
    expected_accuracy : float = MODEL_TRAINER_EXPECTED_SCORE
    model_config_file_path : str = MODEL_TRAINER_MODEL_CONFIG_FILE_PATH
    
    # directory to store all tuned model reports
    # artifact/timestamp/model_trainer/"all_model_report"/"all_tuned_model_report.yaml" 
    all_models_report_file_path : str = os.path.join(
        model_trainer_dir , MODEL_TRAINER_ALL_MODEL_REPORT_DIR , MODEL_TRAINER_ALL_TUNED_MODEL_REPORT_FILE_PATH
    )

