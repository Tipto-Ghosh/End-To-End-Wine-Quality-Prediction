import os
import sys 
import pandas as pd 
from typing import Optional
from dataclasses import dataclass
from sklearn.metrics import accuracy_score

from wineQuality.exception import WineException
from wineQuality.logger import logging
from wineQuality.constants import TARGET_COLUMN
from wineQuality.entity.estimator import WineQualityEstimator
from wineQuality.entity.artifact_entity import DataTransformationArtifact , ModelEvaluationArtifact , ModelTrainerArtifact
from wineQuality.entity.config_entity import ModelEvaluationConfig
from wineQuality.utils.main_utils import load_object , load_numpy_array_data


class ModelEvaluation:
    
    def __init__(self , model_evaluation_config: ModelEvaluationConfig , data_transformation_artifact: DataTransformationArtifact , model_trainer_artifact: ModelTrainerArtifact):
        try:
            self.model_evaluation_config = model_evaluation_config
            self.data_transformation_artifact = data_transformation_artifact
            self.model_trainer_artifact = model_trainer_artifact
        except Exception as e:
            raise WineException(e , sys)
    
    def get_production_model(self) -> Optional[WineQualityEstimator]:
        """This function is used to get model in production

        Returns:
            Optional[WineQualityEstimator]: Returns model object if available in production
        """
        
        try:
            production_model_path = self.model_evaluation_config.production_model_path
            # check do we have any model?
            if not os.path.exists(production_model_path):
                logging.info("No production model file found at path: %s", production_model_path)
                return None 
            # load the model
            production_model_object = load_object(production_model_path)
            if production_model_object is None:
                logging.info("No model found in production")
                return None 
            else:
                logging.info(f"Model found in production. Type: {type(production_model_object)}")
                return production_model_object
        except Exception as e:
            raise WineException(e , sys)
    
    
    def evaluate_model(self) -> ModelEvaluationArtifact:
        """This function is used to evaluate trained model with production model and choose best model 

        Returns:
            ModelEvaluationArtifact: ModelEvaluationArtifact object
        """
        
        try:
            # load the transformed test data
            test_arr = load_numpy_array_data(self.data_transformation_artifact.transformed_test_data_file_path)
            logging.info(f"test array loaded from evaluate_model. shape: [{test_arr.shape}]")
            
            input_feature_arr , target_feature_arr = test_arr[: , : -1] , test_arr[: , -1]
            logging.info(f"from model evaluation seperated input and target feature. input shape:[{input_feature_arr.shape}] , target_feature shape: [{target_feature_arr.shape}]")
            
            # load both new and production model
            new_trained_model = load_object(self.model_trainer_artifact.trained_model_file_path)
            
            if new_trained_model is None:
                logging.info("Failed to load new trained model")
                raise Exception("Failed to load new trained model")
            
            production_model = self.get_production_model()
            if production_model is not None: 
                y_pred_production_model = production_model.predict(input_feature_arr)
                production_model_accuracy = accuracy_score(
                    y_true = target_feature_arr , y_pred = y_pred_production_model
                )
            else:
                production_model_accuracy = 0
            
            # now calculate one new trained model
            y_pred_new_trained_model = new_trained_model.predict(input_feature_arr)
            new_trained_model_accuracy = accuracy_score(
                y_true = target_feature_arr , y_pred = y_pred_new_trained_model
            )
            logging.info(f"New trained model accuracy on test data: {new_trained_model_accuracy}")
            
            is_model_accepted = new_trained_model_accuracy > production_model_accuracy
            accuracy_score_difference = new_trained_model_accuracy - production_model_accuracy
            
            if is_model_accepted:
                best_model_path = self.model_trainer_artifact.trained_model_file_path
            else:
                best_model_path = self.model_evaluation_config.production_model_path
            
            model_evaluation_artifact = ModelEvaluationArtifact(
                is_model_accepted = is_model_accepted ,
                improved_accuracy = accuracy_score_difference,
                best_model_path = best_model_path
            )
            logging.info(f"result: {model_evaluation_artifact}")
            logging.info("Exiting from evaluate_model method of ModelEvaluation class")
            return model_evaluation_artifact
            
        except Exception as e:
            raise WineException(e , sys)
    
    def initiate_model_evaluation(self) -> ModelEvaluationArtifact:
        """This method is used to initialize all the steps of the model evaluation

        Returns:
            ModelEvaluationArtifact: ModelEvaluationArtifact object
        """
        try:
            return self.evaluate_model()
        except Exception as e:
            raise WineException(e , sys)