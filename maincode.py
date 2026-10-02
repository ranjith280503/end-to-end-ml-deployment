
import pandas as pd
import joblib
from fastapi import FastAPI, Form
app = FastAPI()

import joblib
model = joblib.load("penguins_model.pkl")
@app.get("/")
def home():
    return {"message": "ML Model API is running"}
@app.post("/predict")
def predict(
    bill_length_mm: float = Form(...),
    bill_depth_mm: float = Form(...),
    flipper_length_mm: float = Form(...),
    body_mass_g: float = Form(...),
    island: str = Form(...),
    sex: str = Form(...)
):

    input_data = pd.DataFrame([{
        "bill_length_mm": bill_length_mm,
        "bill_depth_mm": bill_depth_mm,
        "flipper_length_mm": flipper_length_mm,
        "body_mass_g": body_mass_g,
        "island": island,
        "sex": sex
    }])

    prediction = model.predict(input_data)

    return {
        "prediction": prediction[0]
    }