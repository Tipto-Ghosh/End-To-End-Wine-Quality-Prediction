# End-To-End-Wine-Quality-Prediction
The Wine Quality Prediction project focuses on building an end-to-end machine learning pipeline that predicts the quality of wine based on its physicochemical properties.

`Dataset is given here: `[Wine Data](https://www.kaggle.com/datasets/ruthgn/wine-quality-data-set-red-white-wine)

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
   pip install -r requirments.txt
```

### 6. Install the project in editable mode (for development)
   - check requirments.txt, if  `-e .` is commented `# -e .` then run this otherwise skip.
   ```bash
      pip install -e .
   ``` 

## Project Structure
```bash
    End-To-End-Wine-Quality-Prediction/
    │
    ├── wineQuality/                  # Main package
    │   ├── components/                 # Data pipeline components
    │   │   ├── data_ingestion.py
    │   │   ├── data_validation.py
    │   │   ├── data_transformation.py
    │   │   ├── model_trainer.py
    │   │   ├── model_evaluation.py
    │   │   ├── model_pusher.py
    │   │   └── __init__.py
    │   │
    │   ├── configuration/              # Configuration manager
    │   │   └── __init__.py
    │   │
    │   ├── constants/                  # Global constants
    │   │   └── __init__.py
    │   │
    │   ├── entity/                     # Entity classes
    │   │   ├── config_entity.py
    │   │   ├── artifact_entity.py
    │   │   └── __init__.py
    │   │
    │   ├── exception/                  # Custom exceptions
    │   │   └── __init__.py
    │   │
    │   ├── logger/                     # Logging utilities
    │   │   └── __init__.py
    │   │
    │   ├── utils/                      # Helper functions
    │   │   ├── main_utils.py
    │   │   └── __init__.py
    │   │
    │   ├── pipeline/                   # Training & prediction pipelines
    │   │   ├── training_pipeline.py
    │   │   ├── prediction_pipeline.py
    │   │   └── __init__.py
    │   │
    │   └── __init__.py
    │
    ├── config/                         # Config & schema files
    │   ├── params.yaml
    │   └── schema.yaml
    │
    ├── notebooks/                      # Jupyter notebooks
    │   └── EDA.ipynb
    │
    ├── static/                         # Static assets
    │   └── css/
    │       └── style.css
    │
    ├── templates/                      # HTML templates
    │   └── index.html
    │
    ├── main.py                         # Project entry point
    ├── app.py                          # Streamlit app entry
    ├── demo.py                         # Quick demo/testing script
    ├── requirements.txt                # Dependencies
    └── setup.py                        # Package setup
```
