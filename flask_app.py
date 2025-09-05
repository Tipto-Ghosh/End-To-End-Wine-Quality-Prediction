import os
from flask import Flask, request, render_template, jsonify
import pandas as pd

from wineQuality.entity.estimator import WineQualityEstimator
from wineQuality.utils.main_utils import load_object
from wineQuality.constants import PRODUCTION_MODEL_PATH, PRODUCTION_PREPROCESSOR_PATH

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def predict():
    # Initial GET request: render HTML without prediction
    if request.method == "GET":
        return render_template("wine_quality.html")

    # POST request: return JSON for AJAX
    if request.method == "POST":
        try:
            # Get form data
            wine_type = request.form.get("wine_type")
            fixed_acidity = float(request.form.get("fixed_acidity"))
            volatile_acidity = float(request.form.get("volatile_acidity"))
            citric_acid = float(request.form.get("citric_acid"))
            residual_sugar = float(request.form.get("residual_sugar"))
            chlorides = float(request.form.get("chlorides"))
            free_sulfur_dioxide = float(request.form.get("free_sulfur_dioxide"))
            total_sulfur_dioxide = float(request.form.get("total_sulfur_dioxide"))
            density = float(request.form.get("density"))
            pH = float(request.form.get("pH"))
            sulphates = float(request.form.get("sulphates"))
            alcohol = float(request.form.get("alcohol"))

            # Create input dataframe
            input_df = pd.DataFrame([{
                "wine type": wine_type,
                "fixed acidity": fixed_acidity,
                "volatile acidity": volatile_acidity,
                "citric acid": citric_acid,
                "residual sugar": residual_sugar,
                "chlorides": chlorides,
                "free sulfur dioxide": free_sulfur_dioxide,
                "total sulfur dioxide": total_sulfur_dioxide,
                "density": density,
                "pH": pH,
                "sulphates": sulphates,
                "alcohol": alcohol
            }])

            # Load preprocessor and model
            preprocessor = load_object(PRODUCTION_PREPROCESSOR_PATH)
            model = load_object(PRODUCTION_MODEL_PATH)

            # Make estimator
            estimator = WineQualityEstimator(
                preprocessing_object=preprocessor,
                trained_model_object=model
            )

            # Predict
            prediction = estimator.predict_dataframe(input_df)[0]
            print(f"Prediction Result: {prediction}")

            # Return JSON for your JS fetch
            return jsonify({"prediction": prediction})

        except Exception as e:
            print("Error during prediction:", str(e))
            return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
