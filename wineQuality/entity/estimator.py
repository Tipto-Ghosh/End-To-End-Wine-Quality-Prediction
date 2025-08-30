import sys 
import warnings
warnings.filterwarnings("ignore")

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