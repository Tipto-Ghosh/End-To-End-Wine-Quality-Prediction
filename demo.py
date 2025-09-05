import sys 
from wineQuality.exception import WineException
from wineQuality.logger import logging
from wineQuality.constants import SCHEMA_FILE_PATH
from wineQuality.utils.main_utils import read_yaml_file , load_numpy_array_data , load_object
from wineQuality.entity.estimator import WineQualityEstimator

import pandas as pd

schema_file_content = read_yaml_file(SCHEMA_FILE_PATH)

# print(f"All Columns: {schema_file_content['columns'].keys()}")
# print(" - " * 40)
# print(f"Numerical columns: {schema_file_content['numerical_columns'].keys()}")
# print(" - " * 40)
# print(f"categorical_columns: {schema_file_content['categorical_columns'].keys()}")

# columns = ['quality']
# missing = []
# for col in schema_file_content['numerical_columns']:
#     if col not in columns:
#         missing.append(col)

# drop_cols = schema_file_content["drop_columns"]
# print(drop_cols)

# log_col = schema_file_content["log_transformation"]
# print(log_col)

# sqrt_col = schema_file_content["sqrt_transformation"]
# print(sqrt_col)

# others = schema_file_content["other_columns"]
# print(others)

preprocessor = load_object("production/preprocessor.pkl")
model = load_object("production/model.pkl")

estimator = WineQualityEstimator(preprocessing_object = preprocessor , trained_model_object = model)

user_input = pd.DataFrame([{
    "wine type": "red",
    "fixed acidity": 10.5,
    "volatile acidity": 0.59,
    "citric acid": 0.49,
    "residual sugar": 2.1,
    "chlorides": 0.07,
    "free sulfur dioxide": 14.0,
    "total sulfur dioxide": 47.0,
    "density": 0.9991,
    "pH": 3.3,
    "sulphates": 0.56,
    "alcohol": 9.6
}])

predicted_label = estimator.predict_dataframe(user_input)
print(predicted_label)