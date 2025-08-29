import os 
import sys 

import numpy as np
import dill
import yaml
from pandas import DataFrame
import pandas as pd 
from wineQuality.logger import logging
from wineQuality.exception import WineException


def read_csv(file_path: str) -> DataFrame:
    """
    Read a CSV file into a Pandas DataFrame.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        DataFrame: Pandas DataFrame containing the data from the CSV file.

    Raises:
        WineException: If reading the CSV file fails.
    """
    logging.info(f"Entered read_csv with file_path={file_path}")
    try:
        df = pd.read_csv(file_path)
        logging.info(f"CSV file loaded successfully: {file_path}, shape={df.shape}")
        return df
    except Exception as e:
        logging.error(f"Error occurred while reading CSV file: {file_path}")
        raise WineException(e, sys)  
    

def read_yaml_file(file_path: str) -> dict:
    """
    Read a YAML file and return its content as a dictionary.

    Args:
        file_path (str): Path to the YAML file.

    Returns:
        dict: Parsed content of the YAML file.

    Raises:
        WineException: If reading the YAML file fails.
    """
    
    logging.info(f"Entered read_yaml_file with file_path={file_path}")
    try:
        with open(file_path, "rb") as yaml_file:
            data = yaml.safe_load(yaml_file)
        logging.info(f"YAML file loaded successfully: {file_path}")
        return data
    except Exception as e:
        logging.error(f"Error occurred while reading YAML file: {file_path}")
        raise WineException(e, sys)  
    

def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    """
    Write content to a YAML file.

    Args:
        file_path (str): Path where the YAML file should be saved.
        content (object): The content to write (usually a dict).
        replace (bool, optional): Whether to replace an existing file. Defaults to False.

    Raises:
        WineException: If writing the YAML file fails.
    """
    
    logging.info(f"Entered write_yaml_file with file_path={file_path}, replace={replace}")
    try:
        if replace and os.path.exists(file_path):
            os.remove(file_path)
            logging.info(f"Existing file removed: {file_path}")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            yaml.dump(content, file)
        logging.info(f"YAML file written successfully: {file_path}")
    except Exception as e:
        logging.error(f"Error occurred while writing YAML file: {file_path}")
        raise WineException(e, sys)  
    

def save_object(file_path: str, obj: object) -> None:
    """
    Save a Python object to disk using dill.

    Args:
        file_path (str): Path where the object should be saved.
        obj (object): Python object to save.

    Raises:
        WineException: If saving the object fails.
    """
    
    logging.info(f"Entered save_object with file_path={file_path}")
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
        logging.info(f"Object saved successfully at: {file_path}")
    except Exception as e:
        logging.error(f"Error occurred while saving object: {file_path}")
        raise WineException(e, sys)  
        

def load_object(file_path: str) -> object:
    """
    Load a Python object from disk using dill.

    Args:
        file_path (str): Path to the object file.

    Returns:
        object: Loaded Python object.

    Raises:
        WineException: If loading the object fails.
    """
    
    logging.info(f"Entered load_object with file_path={file_path}")
    try:
        with open(file_path, "rb") as file_obj:
            obj = dill.load(file_obj)
        logging.info(f"Object loaded successfully from: {file_path}")
        return obj
    except Exception as e:
        logging.error(f"Error occurred while loading object: {file_path}")
        raise WineException(e, sys)  
        

def save_numpy_array_data(file_path: str, array: np.array):
    """
    Save a NumPy array to disk.

    Args:
        file_path (str): Path where the array should be saved.
        array (np.ndarray): NumPy array to save.

    Raises:
        WineException: If saving the array fails.
    """
    
    logging.info(f"Entered save_numpy_array_data with file_path={file_path}, array_shape={array.shape}")
    try:
        dir_path = os.path.dirname(file_path)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            np.save(file_obj, array)
        logging.info(f"NumPy array saved successfully at: {file_path}")
    except Exception as e:
        logging.error(f"Error occurred while saving numpy array: {file_path}")
        raise WineException(e, sys)  
    

def load_numpy_array_data(file_path: str) -> np.array:
    """
    Load a NumPy array from disk.

    Args:
        file_path (str): Path to the NumPy file.

    Returns:
        np.ndarray: Loaded NumPy array.

    Raises:
        WineException: If loading the array fails.
    """
    
    logging.info(f"Entered load_numpy_array_data with file_path={file_path}")
    try:
        with open(file_path, 'rb') as file_obj:
            array = np.load(file_obj)
        logging.info(f"NumPy array loaded successfully from: {file_path}, array_shape={array.shape}")
        return array
    except Exception as e:
        logging.error(f"Error occurred while loading numpy array: {file_path}")
        raise WineException(e, sys)  
    

def drop_columns(df: DataFrame, cols: list)-> DataFrame:
    """
    Drop specific columns from a Pandas DataFrame.

    Args:
        df (DataFrame): Input Pandas DataFrame.
        cols (list): List of column names to drop.

    Returns:
        DataFrame: DataFrame with specified columns removed.

    Raises:
        WineException: If dropping columns fails.
    """
    
    logging.info(f"Entered drop_columns with cols={cols}")
    try:
        df = df.drop(columns=cols, axis=1)
        logging.info(f"Dropped columns: {cols}, new_shape={df.shape}")
        return df
    except Exception as e:
        logging.error(f"Error occurred while dropping columns: {cols}")
        raise WineException(e, sys)  
    

def save_yaml_file(file_path: str, data: dict):
    """
    Save dictionary data to a YAML file.

    Args:
        file_path (str): Path where the YAML file should be saved.
        data (dict): Dictionary data to save.

    Raises:
        WineException: If saving the YAML file fails.
    """
    logging.info(f"Entered save_yaml_file with file_path={file_path}")
    try:
        dir_path = os.path.dirname(file_path)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'w') as file_obj:
            yaml.dump(data, file_obj)
        logging.info(f"YAML file saved successfully: {file_path}")
    except Exception as e:
        logging.error(f"Error occurred while saving YAML file: {file_path}")
        raise WineException(e, sys)  

def save_csv_file(file_path: str, data: pd.DataFrame):
    """
    Save a pandas DataFrame to a CSV file.

    Args:
        file_path (str): Path where the CSV file should be saved.
        data (pd.DataFrame): DataFrame to save.

    Raises:
        WineException: If saving the CSV file fails.
    """
    logging.info(f"Entered save_csv_file with file_path={file_path}")
    try:
        dir_path = os.path.dirname(file_path)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)
        data.to_csv(file_path, index=False)
        logging.info(f"CSV file saved successfully: {file_path}")
    except Exception as e:
        logging.error(f"Error occurred while saving CSV file: {file_path}")
        raise WineException(e, sys)  