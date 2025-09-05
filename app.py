import streamlit as st
import pandas as pd 
from wineQuality.entity.estimator import WineQualityEstimator
from wineQuality.constants import PRODUCTION_MODEL_PATH, PRODUCTION_PREPROCESSOR_PATH
from wineQuality.utils.main_utils import load_object

# --- Set wide layout to fit all columns ---
st.set_page_config(layout="wide")
st.title("Wine Quality Prediction 🍷")
st.write("Enter wine features to predict whether it's Standard or Premium")

# --- Wine type ---
wine_type = st.selectbox("Wine type", ["red", "white"])

# --- 4 columns layout for numeric inputs ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    fixed_acidity = st.number_input("Fixed Acidity", min_value=0.0, value=7.0, format="%.2f")
    volatile_acidity = st.number_input("Volatile Acidity", min_value=0.0, value=0.3, format="%.2f")
    citric_acid = st.number_input("Citric Acid", min_value=0.0, value=0.3, format="%.2f")

with col2:
    residual_sugar = st.number_input("Residual Sugar", min_value=0.0, value=2.0, format="%.2f")
    chlorides = st.number_input("Chlorides", min_value=0.0, value=0.05, format="%.3f")
    free_sulfur_dioxide = st.number_input("Free Sulfur Dioxide", min_value=0.0, value=15.0, format="%.1f")

with col3:
    total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide", min_value=0.0, value=46.0, format="%.1f")
    density = st.number_input("Density", min_value=0.0, value=0.998, format="%.5f")
    pH = st.number_input("pH", min_value=0.0, value=3.3, format="%.2f")

with col4:
    sulphates = st.number_input("Sulphates", min_value=0.0, value=0.5, format="%.2f")
    alcohol = st.number_input("Alcohol", min_value=0.0, value=9.0, format="%.2f")

# --- Prediction button and result ---
predict_col, result_col = st.columns([1, 2])

with predict_col:
    if st.button("Predict Wine Quality"):
        # Create input dataframe
        input_df = pd.DataFrame([{
            "wine type"            : wine_type,
            "fixed acidity"        : fixed_acidity,
            "volatile acidity"     : volatile_acidity,
            "citric acid"          : citric_acid,
            "residual sugar"       : residual_sugar,
            "chlorides"            : chlorides,
            "free sulfur dioxide"  : free_sulfur_dioxide,
            "total sulfur dioxide" : total_sulfur_dioxide,
            "density"              : density,
            "pH"                   : pH,
            "sulphates"            : sulphates,
            "alcohol"              : alcohol
        }])
        
        # Load preprocessor and model
        preprocessing_object = load_object(file_path = PRODUCTION_PREPROCESSOR_PATH)
        model_object = load_object(file_path = PRODUCTION_MODEL_PATH)
        
        # Initialize estimator
        estimator = WineQualityEstimator(
            preprocessing_object = preprocessing_object,
            trained_model_object = model_object
        )
        
        # Predict
        predicted_label = estimator.predict_dataframe(input_df = input_df)
        
        with result_col:
            st.success(f"The predicted wine category is: {predicted_label[0]}")
