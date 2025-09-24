from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging

import joblib

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

try:
    model_path = '/models/trained_model.joblib'
    logger.info(f"Loading model from: {model_path}")
    model = joblib.load(model_path)

    logger.info("Model loaded successfully")

except Exception as e:
    logger.error(f"Error loading model: {e}")
    model = None

class DiabetesFeatures(BaseModel):
    age: float
    sex: float
    bmi: float
    bp: float
    s1: float
    s2: float
    s3: float
    s4: float
    s5: float
    s6: float

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/predict")
def predict(features: DiabetesFeatures):
    try:
        data = list(features.model_dump().values())
        logger.info(f"Received request with data: {data}")

        prediction = model.predict([data])

        prediction = float(prediction[0])

        logger.info(f"Prediction {prediction} for values {features.model_dump()}")
        return {
            "prediction": prediction,
        }
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")