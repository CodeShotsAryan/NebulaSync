from fastapi import FastAPI
from .api.health_risk import predict_health_risk  
from .services.health_risk import health_risk_model, predict_health_risk
from .schemas.health_risk import HealthRiskData

app = FastAPI()

@app.post('/predict_health_risk')
async def predict_health_risk_endpoint(data:HealthRiskData):
    result = predict_health_risk(data)
    return result 