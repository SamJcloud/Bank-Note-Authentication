import uvicorn
from fastapi import FastAPI
import pandas as pd 
import joblib
from pydantic import BaseModel

app = FastAPI()

class Banknote(BaseModel):
    variance: float
    skewness: float
    curtosis: float
    entropy: float


model = joblib.load("gbc_model.joblib")


@app.get("/")
def read_root():
    return {"message": "Banknote Authentication API is running."}

@app.post("/predict")
def predict(banknote: Banknote):
    data = [[
        banknote.variance,
        banknote.skewness,
        banknote.curtosis,
        banknote.entropy
    ]]
    df = pd.DataFrame(data, columns=['variance', 'skewness', 'curtosis', 'entropy'])
    prediction = model.predict(df)[0]
    if prediction == 0:
        return {"prediction": "Fake note"}
    else:
        return {"prediction": "Its a real note"}
    

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)

        