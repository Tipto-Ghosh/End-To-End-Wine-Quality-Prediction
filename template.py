import os
from pathlib import Path
import logging


logging.basicConfig(level = logging.INFO , format = '[%(asctime)s]: %(message)s:')

project_name = "wineQuality"

list_of_files = [
    f"{project_name}/__init__.py",
    
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    
    f"{project_name}/configuration/__init__.py",
    
    f"{project_name}/constants/__init__.py",
    
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    

    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    
    "config/params.yaml",
    "config/schema.yaml",
    
    "notebooks/mongoDbDataPush.ipynb",
    
    "main.py",
    "app.py",
    "demo.py",
    
    "requirements.txt",
    "setup.py",
    ".env",
    
    "static/css/style.css",
    "templates/index.html",
]

# Go to the list items and create's all the folder's and files
for filepath in list_of_files:
    
    filepath = Path(filepath)
    filedir , filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir , exist_ok = True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath , "w") as f:
            pass 
        
        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")