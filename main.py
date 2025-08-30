import warnings
warnings.filterwarnings("ignore")

from wineQuality.pipeline.training_pipeline import TrainingPipeline 

# Run the training pipeline
training_pipeline_obj = TrainingPipeline()
training_pipeline_obj.run_training_pipeline()