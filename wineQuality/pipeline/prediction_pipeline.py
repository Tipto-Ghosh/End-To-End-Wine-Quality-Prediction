import sys
import pandas as pd

from wineQuality.exception import WineException
from wineQuality.logger import logging
from wineQuality.utils.main_utils import load_object
from wineQuality.entity.config_entity import WineQualityPredictionConfig


class WineQualityPredictionPipeline:
    
    def __init__(self , config: WineQualityPredictionConfig = WineQualityPredictionConfig()):
        try:
            self.config = config
            
            logging.info("Loading preprocessor and model from production...")
            self.preprocessor = load_object(self.config.preprocessor_file_path)
            self.model = load_object(self.config.model_file_path)
            
            
            if self.preprocessor is None or self.model is None:
                raise Exception("Preprocessor or Model could not be loaded from production.")
            
            logging.info("Preprocessor and Model successfully loaded.")
        except Exception as e:
            raise WineException(e , sys)