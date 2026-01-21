import joblib
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
model = joblib.load("models/random_forest.pkl")

class Metrics(BaseModel):
    cpu: float
    memory: float
    disk_io: float
    pod_restarts: int
    latency: float

@app.post("/predict")
def predict(metrics: Metrics):
    features = [[
        metrics.cpu,
        metrics.memory,
        metrics.disk_io,
        metrics.pod_restarts,
        metrics.latency
    ]]

    probability = model.predict_proba(features)[0][1]

    return {
        "failure_probability": round(float(probability), 2),
        "trigger_dr": probability > 0.80
    }

