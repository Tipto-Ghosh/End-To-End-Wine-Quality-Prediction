from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:
    train_data_file_path: str 
    test_data_file_path: str 