# 🧠 Banknote Authentication API

A lightweight FastAPI app for authenticating banknotes using a trained Gradient Boosting Classifier.

## 🚀 Features

- Accepts 4 numerical inputs: `variance`, `skewness`, `curtosis`, `entropy`
- Predicts whether a banknote is **real or fake**
- Built with `FastAPI`, `scikit-learn`, and `joblib`

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/your-username/banknote-api.git
cd banknote-api

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

🧪 Running the API
```bash
uvicorn app:app --reload
```
Visit http://127.0.0.1:8000/docs for the interactive Swagger UI.

🧠 Model
This app uses a pre-trained GradientBoostingClassifier saved as gbc_model.joblib. Train your model separately and ensure it's saved in the project directory.

🔍 API Endpoint
POST /predict
```json
{
  "variance": 2.3,
  "skewness": 6.7,
  "curtosis": -2.4,
  "entropy": 0.5
}
```
Response
```json
{
  "prediction": "Real note"
}
```
🧰 Tools
Python 3.12
FastAPI
scikit-learn
Uvicorn
