# End-To-End Wine Quality Prediction

The **Wine Quality Prediction** project is an end-to-end machine learning pipeline designed to predict the quality of wine based on its physicochemical properties. This project covers the complete ML lifecycle, including data ingestion, validation, transformation, model training, evaluation, and deployment through both Flask and Streamlit apps.

**Dataset:** [Wine Data](https://www.kaggle.com/datasets/ruthgn/wine-quality-data-set-red-white-wine)

---

## 🗂 Project Structure

```bash
End-To-End-Wine-Quality-Prediction/
│
├── wineQuality/                  # Main package
│   ├── components/               # Data pipeline components
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │   ├── model_evaluation.py
│   │   ├── model_pusher.py
│   │   └── __init__.py
│   │
│   ├── configuration/            # Configuration manager
│   │   └── __init__.py
│   │
│   ├── constants/                # Global constants
│   │   └── __init__.py
│   │
│   ├── entity/                   # Entity classes
│   │   ├── config_entity.py
│   │   ├── artifact_entity.py
│   │   └── __init__.py
│   │
│   ├── exception/                # Custom exceptions
│   │   └── __init__.py
│   │
│   ├── logger/                   # Logging utilities
│   │   └── __init__.py
│   │
│   ├── utils/                    # Helper functions
│   │   ├── main_utils.py
│   │   └── __init__.py
│   │
│   ├── pipeline/                 # Training & prediction pipelines
│   │   ├── training_pipeline.py
│   │   ├── prediction_pipeline.py
│   │   └── __init__.py
│   │
│   └── __init__.py
│
├── config/                       # Config & schema files
│   ├── params.yaml
│   └── schema.yaml
│
├── notebooks/                     # Jupyter notebooks
│   └── EDA.ipynb
│
├── static/                        # Static assets
│   └── css/
│       └── style.css
│
├── templates/                     # HTML templates
│   └── index.html
│
├── main.py                        # Project entry point
├── app.py                         # Streamlit app entry
├── flaskApp.py                    # Flask app entry
├── demo.py                        # Quick demo/testing script
├── requirements.txt               # Dependencies
└── setup.py                       # Package setup
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Tipto-Ghosh/End-To-End-Wine-Quality-Prediction.git
```

### 2. Navigate into the project directory
```bash
cd End-To-End-Wine-Quality-Prediction
```

### 3. Create a virtual environment
```bash
python -m venv venv
```

### 4. Activate the virtual environment
- **Windows (PowerShell)**
```bash
.\venv\Scripts\Activate
```
- **Linux/macOS**
```bash
source venv/bin/activate
```

### 5. Install dependencies
```bash
pip install -r requirements.txt
```

### 6. Install the project in editable mode (optional)
```bash
pip install -e .
```

---

## ⚡ Retraining Models (Optional)

1. Create a [MongoDB](https://account.mongodb.com/account/login) account and a cluster.
2. Save the connection string in a `.env` file:
```env
DATABASE_URL="Your connection string"
```
3. Push dataset to MongoDB by running the notebook `mongoDbDataPush.ipynb`.
4. Train the models using:
```bash
python main.py
```

---

## 💻 Running the Application

### Streamlit
```bash
streamlit run app.py
```

### Flask
```bash
python flaskApp.py
```

---

## 📊 Model Performance

### Without Hyperparameter Tuning

| Model Name                  | Accuracy  |
|------------------------------|-----------|
| Random Forest               | 0.9544    |
| XGBClassifier               | 0.9433    |
| CatBoosting Classifier      | 0.9339    |
| K-Neighbors Classifier      | 0.9330    |
| Decision Tree               | 0.9256    |
| Gradient Boosting           | 0.8828    |
| Support Vector Classifier   | 0.8716    |
| AdaBoost Classifier         | 0.8316    |
| Logistic Regression         | 0.8223    |

### With Hyperparameter Tuning of Top-05 Models.

| Model Name                  | Accuracy  |
|------------------------------|-----------|
| KNN Classifier               | 0.9758    |
| CatBoost Classifier          | 0.9600    |
| Random Forest Classifier     | 0.9535    |
| XGBoost Classifier           | 0.9479    |
| Decision Tree Classifier     | 0.9042    |

---

## 🔧 Features

- End-to-end ML pipeline from raw data to deployment.
- Data ingestion, validation, and transformation.
- Supports multiple models: Random Forest, XGBoost, CatBoost, KNN, and more.
- Flask and Streamlit web apps for prediction.
- MongoDB integration for dataset storage.
- Clear, modular, and maintainable code structure.

---

## 📌 License
This project is licensed under the MIT License.

---

## 📫 Contact
- Created by [TiptoGhosh](https://www.linkedin.com/in/tipto-ghosh-4b0aab283/) – feel free to connect via Linkedin.
- Also you can mail me on this address: [tipto_ghosh](tiptoghosh@gmail.com)

