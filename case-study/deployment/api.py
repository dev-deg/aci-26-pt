from enum import Enum
from pathlib import Path
from typing import List

import joblib
import numpy as np
import pandas as pd

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

BASE_DIR = Path(__file__).parent
MODEL_PATH = BASE_DIR / "hgb_price-Model.joblib"

if not MODEL_PATH.exists():
    raise RuntimeError(f"{MODEL_PATH} not found - run the notebook first to create it.")

## model, feature list, category levels, defaults, metrics
artifact = joblib.load(MODEL_PATH)

app = FastAPI(title="Malta Airbnb Price API", version="1.0.0")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

RoomType = Enum("RoomType", {v: v for v in artifact["categories"]["room_type"]}, type=str)
Neighbourhood = Enum("Neighbourhood", {v: v for v in artifact["categories"]["neighbourhood"]}, type=str)

# Pydantic Models (input/output validation and documentation)
class Listing(BaseModel):
    room_type: RoomType = Field(..., examples=["Entire home/apt"])
    neighbourhood: Neighbourhood = Field(..., examples=["Sliema"])
    minimum_nights: int = Field(..., ge=1, examples=[2])

class Prediction(BaseModel):
    predicted_price_eur: float

def predict(listings: List[Listing]) -> List[Prediction]:
    rows = []
    for listing in listings:
        row = {
            **artifact["numeric_defaults"],
            **listing.model_dump(mode="json"),
            **artifact["location_defaults"].get(listing.neighbourhood.value, {}),
        }
        rows.append(row)
    df = pd.DataFrame(rows)[artifact["feature_cols"]]

    # Convert categorical columns to the correct dtype
    # This is necessary for the model to work correctly
    for col, categories in artifact["categories"].items():
        df[col] = pd.Categorical(df[col], categories=categories)

    # Make predictions
    # The model was trained on log1p(price), so we need to apply expm1 to get back to the original scale
    prices = np.clip(np.expm1(artifact["model"].predict(df)), 0, None)  # expm1 because we trained on log1p(price)
    return [Prediction(predicted_price_eur=price) for price in prices]

# Endpoint to return html page
@app.get("/", response_class=FileResponse)
def index():
    return BASE_DIR / "index.html"

#Endpoint for different room types and neighbourhoods
@app.get("/room-types", response_model=List[str])
def room_types():
    return list(artifact["categories"]["room_type"])

@app.get("/neighbourhoods", response_model=List[str])
def neighbourhoods():
    return list(artifact["categories"]["neighbourhood"])

@app.get("/metadata")
def metadata():
    return {
        "model": artifact["model"].__class__.__name__,
        "metrics": artifact["metrics"],
    }

@app.post("/predict", response_model=Prediction)
def predict_endpoint(listing: Listing):
    return predict([listing])[0]

@app.post("/predict/batch", response_model=List[Prediction])
def predict_batch_endpoint(listings: List[Listing]):
    return predict(listings)