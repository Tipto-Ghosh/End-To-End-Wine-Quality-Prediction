from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:
    train_data_file_path: str 
    test_data_file_path: str


@dataclass
class DataValidationArtifact:
    train_data_file_path: str 
    test_data_file_path: str
    data_validation_status : bool 
    data_drift_report_file_path : str 


@dataclass
class DataTransformationArtifact:
    transformed_object_file_path : str
    transformed_train_data_file_path : str
    transformed_test_data_file_path : str 


@dataclass
class ClassificationMetricArtifact:
    accuracy_score : float
    f1_score : float
    precision_score : float
    recall_score : float
    
@dataclass
class ModelTrainerArtifact:
    trained_model_file_path : str 
    metric_artifact : ClassificationMetricArtifact
    tuned_model_report_file_path : str