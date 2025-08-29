import sys 
from wineQuality.exception import WineException
from wineQuality.logger import logging
from wineQuality.constants import SCHEMA_FILE_PATH
from wineQuality.utils.main_utils import read_yaml_file


schema_file_content = read_yaml_file(SCHEMA_FILE_PATH)

# print(f"All Columns: {schema_file_content['columns'].keys()}")
# print(" - " * 40)
# print(f"Numerical columns: {schema_file_content['numerical_columns'].keys()}")
# print(" - " * 40)
# print(f"categorical_columns: {schema_file_content['categorical_columns'].keys()}")

columns = ['quality']
missing = []
for col in schema_file_content['numerical_columns']:
    if col not in columns:
        missing.append(col)