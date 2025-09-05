import sys 
import warnings
warnings.filterwarnings("ignore")

import numpy as np
from pandas import DataFrame
from sklearn.pipeline import Pipeline

from wineQuality.logger import logging
from wineQuality.exception import WineException
from wineQuality.constants import SCHEMA_FILE_PATH , TARGET_COLUMN
from wineQuality.utils.main_utils import save_object , save_numpy_array_data , read_csv , read_yaml_file , drop_columns



class TargetValueMapping:
    def __init__(self):
        # Define target mapping
        self.Standard: int = 0
        self.Premium: int = 1
    
    def _asdict(self):
        """Return mapping as dict {label: value}"""
        return self.__dict__
    
    def reverse_mapping(self):
        """Return reverse mapping {value: label}"""
        mapping_response = self._asdict()
        return dict(zip(mapping_response.values(), mapping_response.keys()))
    
    
    def wine_label(self , q : int) -> int:
        """Convert wine quality score into classification"""
        return 1 if q > 5 else 0


class WineQualityEstimator:
    def __init__(self , preprocessing_object: Pipeline , trained_model_object: object):
        """This class is responsible to combine preprocessor and sklearn model.
           Also to do prediction for new data.

        Args:
            preprocessing_object (Pipeline): _description_
            trained_model_object (object): _description_
        """
        self.preprocessing_object = preprocessing_object
        self.trained_model_object = trained_model_object
        # read the schema file cause we need to know the drop and transformation column names
        self._schema_config = read_yaml_file(file_path = SCHEMA_FILE_PATH)
        self.drop_cols = self._schema_config["drop_columns"]
    
    def predict_transformed_array(self , transformed_array : np.ndarray) -> np.ndarray:
        """
        Predict using already transformed feature array.
        """
        logging.info("Entered predict_array method of WineQualityEstimator class")
        
        try:
            predictions = self.trained_model_object.predict(transformed_array)
            logging.info(f"Prediction completed on transformed array, shape={predictions.shape}")
            return predictions 
        
        except Exception as e:
            raise WineException(e , sys)    
    
    def predict_dataframe(self , input_df: DataFrame , map_to_label: bool = True) -> np.ndarray:
        """
        Transform raw input DataFrame and predict in one step.
        Expects input_df to have a single row or multiple rows with same feature columns.
        """
        logging.info(f"Entered predict_dataframe method with input shape: {input_df.shape}")
        try:
            df = input_df.copy()
            
            # Drop columns that were dropped in training
            df = df.drop(columns = [col for col in self.drop_cols if col in df.columns] , errors = "ignore")
            
            # Ensure all columns expected by the preprocessor exist
            # missing_cols = [c for c in self.preprocessing_object.get_feature_names_out() if c not in df.columns]
            # For missing columns, fill with 0
            # for c in missing_cols:
            #     df[c] = 0
                
            # transform using preprocessing_object
            transformed_data = self.preprocessing_object.transform(df)
            
            # predict
            predictions = self.trained_model_object.predict(transformed_data)
            
            # do the mapping
            if map_to_label:
                mapper = TargetValueMapping()
                predictions = [mapper.reverse_mapping()[p] for p in predictions]
            
            return predictions
            
        except Exception as e:
            raise WineException(e , sys)
    
    def __repr__(self):
        return f"{type(self.trained_model_object).__name__}()"

    def __str__(self):
        return f"{type(self.trained_model_object).__name__}()"