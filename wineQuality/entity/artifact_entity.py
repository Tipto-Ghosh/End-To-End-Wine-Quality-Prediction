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