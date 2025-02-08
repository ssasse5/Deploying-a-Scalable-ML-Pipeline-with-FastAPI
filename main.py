import os
import numpy as np
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field

from ml.data import apply_label, process_data
from ml.model import inference, load_model

# DO NOT MODIFY
class Data(BaseModel):
    age: int = Field(..., example=37)
    workclass: str = Field(..., example="Private")
    fnlgt: int = Field(..., example=178356)
    education: str = Field(..., example="HS-grad")
    education_num: int = Field(..., example=10, alias="education-num")
    marital_status: str = Field(..., example="Married-civ-spouse", alias="marital-status")
    occupation: str = Field(..., example="Prof-specialty")
    relationship: str = Field(..., example="Husband")
    race: str = Field(..., example="White")
    sex: str = Field(..., example="Male")
    capital_gain: int = Field(..., example=0, alias="capital-gain")
    capital_loss: int = Field(..., example=0, alias="capital-loss")
    hours_per_week: int = Field(..., example=40, alias="hours-per-week")
    native_country: str = Field(..., example="United-States", alias="native-country")

encoder_path = "model/encoder.pkl"
model_path = "model/model.pkl"

try:
    encoder = load_model(encoder_path)
    model = load_model(model_path)
except Exception as e:
    print(f"Error loading model or encoder: {e}")
    encoder, model = None, None

# Create a RESTful API using FastAPI
app = FastAPI()

# Create a GET on the root giving a welcome message
@app.get("/")
async def get_root():
    return {"message": "Welcome to the FastAPI ML Model Inference API!"}

# Create a POST on a different path that does model inference
@app.post("/data/")
async def post_inference(data: Data):
    if model is None or encoder is None:
        return {"error": "Model or encoder not loaded properly."}

    data_dict = data.dict()
    data = {k.replace("_", "-"): [v] for k, v in data_dict.items()}
    data = pd.DataFrame.from_dict(data)

    cat_features = [
        "workclass", "education", "marital-status", "occupation", "relationship",
        "race", "sex", "native-country"
    ]
    data_processed, _, _, _ = process_data(
        data, categorical_features=cat_features, training=False, encoder=encoder
    )

    _inference = inference(model, data_processed)
    
    # Debugging print to verify the shape and type of _inference
    print(f"DEBUG: Inference Output: {_inference}")
    print(f"DEBUG: Type of Inference Output: {type(_inference)}")
    
    if isinstance(_inference, (np.ndarray, list)):
        result = apply_label(_inference.item()) # Ensure array indexing is safe
    else:
        result = apply_label(_inference)  # Handle scalar values

    return {"result": result}


