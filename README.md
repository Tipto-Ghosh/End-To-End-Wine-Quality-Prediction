# END-TO-END MACHINE LEARNING PROJECT

# Wine Quality Prediction 🍷
An end-to-end machine learning project to predict wine quality based on physicochemical tests. The project includes data preprocessing, model training using pipelines, and deployment via a Flask web app.

---

## 🔧 Project Workflow

1. Update `config.yaml`  
2. Update `schema.yaml`  
3. Update `params.yaml`  
4. Build entity classes  
5. Create configuration manager in `src/config`  
6. Implement components:
    - Data ingestion  
    - Data validation  
    - Data transformation  
    - Model training  
    - Model evaluation  
7. Build pipeline scripts  
8. Integrate `main.py` to run pipeline  
9. Create `app.py` using Flask for web interface  

---

## 🚀 How to Run?

### ✅ STEPS:

#### 📥 STEP 01 - Clone the Repository

```bash
git clone https://github.com/Tipto-Ghosh/End-To-End-Wine-Quality-Prediction
cd End-To-End-Wine-Quality-Prediction
````

## ⚠️ Python Version Warning

> **⚠️ IMPORTANT:**  
> This project requires **Python 3.11.4**.  
> Do **NOT** use Python 3.12 or 3.13, as many dependencies are **not yet compatible** or may fail during installation.


#### 🐍 STEP 02 - Create a Conda Environment

```bash
conda create -n mlproj python=3.11.4 -y
conda activate mlproj
```
#### ✅ If you are using venv (standard Python):
```bash
python -m venv mlproj
```
##### Activate the environment
###### One Windows
```bash
mlproj\Scripts\activate
```
###### On macOS/Linux:
```bash
source mlproj/bin/activate
```

#### 📦 STEP 03 - Install the Requirements

```bash
pip install -r requirements.txt
```

---

### ▶️ STEP 04 - Run the Application

```bash
python app.py
```

---

## 🌐 Access the App

Open your browser and go to:

```
http://127.0.0.1:5000/
```

---

## 📁 Project Structure

```
project_root/
├── app.py
├── main.py
├── config/
│   └── config.yaml
├── params.yaml
├── schema.yaml
├── src/
│   ├── components/
│   ├── config/
│   ├── entity/
│   ├── pipeline/
│   ├── utils/
│   └── constants/
├── research/
│   ├── find_issues_in_data.ipynb
│   ├── fixinf_issues_in_data.ipynb
│   └── EDA.ipynb
├── templates/
│   └── index.html
├── requirements.txt
├── setup.py
└── README.md
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).