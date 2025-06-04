import os
from pathlib import Path
import logging

# making the logging string
logging.basicConfig(level = logging.INFO , format = '[%(asctime)s]: %(message)s:')

# this is the project name
project_name = "wine-quality-prediction"

# making the file list we need
list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/find_issues_in_data.ipynp",
    "research/fixing_issues_in_data.ipynp",
    "research/EDA.ipynp",
    "templates/index.html"
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