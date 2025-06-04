import os 
from box.exceptions import BoxValueError
import yaml
from wine_quality_prediction import logger
import json
import joblib
from ensure import ensure_annotations # type: ignore
from box import ConfigBox
from pathlib import Path
from typing import Any



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns it as a dot-accessible dictionary (ConfigBox).

    Args:
        path_to_yaml (Path): Path to the YAML configuration file.

    Raises:
        ValueError: If the YAML file is empty or improperly formatted.
        Exception: For any other unexpected errors during file reading.

    Returns:
        ConfigBox: A dictionary-like object allowing dot-notation access.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)  # Load YAML content as a Python dict
            if content is None:
                raise ValueError("YAML file is empty or invalid.")
            logger.info(f"YAML file loaded successfully from: {path_to_yaml}")
            return ConfigBox(content)  # Convert to dot-accessible object
    except BoxValueError:
        raise ValueError("YAML file is empty or contains invalid structure.")
    except Exception as e:
        logger.exception(f"Error while reading YAML file: {path_to_yaml}")
        raise e



@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):
    """
    Creates multiple directories.

    Args:
        path_to_directories (list): List of paths to create
        verbose (bool): whether to log creation info
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok = True)  # Create directory if it doesn't exist
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Saves a Python dictionary as a JSON file.

    Args:
        path (Path): where to save the JSON
        data (dict): dictionary data to save
    """
    with open(path, "w") as f:
        json.dump(data, f, indent = 4)
    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads a JSON file and returns it as dot-accessible ConfigBox.

    Args:
        path (Path): path to the JSON file

    Returns:
        ConfigBox: JSON data with dot notation support
    """
    with open(path) as f:
        content = json.load(f)
    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_binary(data: Any, path: Path):
    """
    Saves any Python object (e.g., model, array) as a binary file using joblib.

    Args:
        data (Any): Python object to save
        path (Path): file path to store binary data
    """
    joblib.dump(value = data, filename = path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_binary(path: Path) -> Any:
    """
    Loads any joblib-saved binary file.

    Args:
        path (Path): binary file path

    Returns:
        Any: loaded Python object
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Returns the size of a file in KB.

    Args:
        path (Path): file path

    Returns:
        str: size as a readable string (e.g., "~ 12 KB")
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

