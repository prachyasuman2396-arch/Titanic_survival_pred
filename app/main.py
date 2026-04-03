from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
from app.schema import PassengerInput
# Initialize app
app = FastAPI(
    title="Titanic Survival Prediction API",
    version="1.0"
)

# Load full pipeline (feature + preprocess + model)
model = joblib.load("/Users/prachyasumandas/Documents/titanic/artifacts/model.pkl")

@app.get("/")
def home():
    return {"message": "Titanic API is running "}


@app.get("/health")
def health():
    return {"status": "ok"}



@app.post("/predict")
def predict(data: PassengerInput):
    
        # Convert input to DataFrame
    input_df = pd.DataFrame([data.model_dump()])

        # Direct prediction (pipeline handles everything)
    prediction = model.predict(input_df)[0]
    probablity = model.predict_proba(input_df)[0][1]
        
    return {
        "survived": int(prediction),
        "survival_probability": float(probablity)
            
    }

    