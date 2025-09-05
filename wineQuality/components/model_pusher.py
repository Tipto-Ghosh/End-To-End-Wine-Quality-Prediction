import os 
import sys 
import shutil

from wineQuality.exception import WineException
from wineQuality.logger import logging

from wineQuality.entity.artifact_entity import ModelEvaluationArtifact , DataTransformationArtifact , ModelPusherArtifact
from wineQuality.entity.config_entity import ModelPusherConfig



class ModelPusher:
    def __init__(self , model_pusher_config: ModelPusherConfig, 
        model_evaluation_artifact: ModelEvaluationArtifact, data_transformation_artifact: DataTransformationArtifact ) -> None:
        
        try:
            self.model_pusher_config = model_pusher_config
            self.model_evaluation_artifact = model_evaluation_artifact
            self.data_transformation_artifact = data_transformation_artifact
        except Exception as e:
            raise WineException(e , sys)
    
    def initiate_model_pusher(self) -> ModelPusherArtifact:
        """
        Pushes the best model and preprocessor to production.
        If they exist, replaces them. If not, creates them.
        """
        try:
            # if model is not accepted
            if not self.model_evaluation_artifact.is_model_accepted:
               logging.info("Model not accepted. Skipping push to production.")
               return ModelPusherArtifact(
                   is_model_pushed = False , 
                   production_model_path = self.model_pusher_config.production_model_path,
                   production_preprocessor_path = self.model_pusher_config.preprocessor_file_path
                )
            
            
            # make production directory(For the first run there will be no directory)
            os.makedirs(os.path.dirname(self.model_pusher_config.production_model_path) , exist_ok = True)
            os.makedirs(os.path.dirname(self.model_pusher_config.preprocessor_file_path) , exist_ok = True)
            
            # replace the model and preprocessor
            shutil.copy(
                src = self.data_transformation_artifact.transformed_object_file_path , 
                dst = self.model_pusher_config.preprocessor_file_path
            )
            logging.info(f"Preprocessor pushed to production: {self.model_pusher_config.preprocessor_file_path}")
            
            shutil.copy(
                src = self.model_evaluation_artifact.best_model_path,
                dst = self.model_pusher_config.production_model_path
            )
            logging.info(f"Model pushed to production: {self.model_pusher_config.production_model_path}")
            
            return ModelPusherArtifact(
                is_model_pushed = True,
                production_model_path = self.model_pusher_config.production_model_path,
                production_preprocessor_path = self.model_pusher_config.preprocessor_file_path
            )
              
        except Exception as e:
             raise WineException(e, sys)