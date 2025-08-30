import sys 
import warnings
warnings.filterwarnings("ignore")

import numpy as np
from pandas import DataFrame
from sklearn.pipeline import Pipeline

from wineQuality.logger import logging
from wineQuality.exception import WineException



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
    
    def __repr__(self):
        return f"{type(self.trained_model_object).__name__}()"

    def __str__(self):
        return f"{type(self.trained_model_object).__name__}()"