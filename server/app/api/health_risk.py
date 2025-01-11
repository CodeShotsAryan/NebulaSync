from fastapi import APIRouter
from ..services.health_risk import predict_health_risk

router = APIRouter()

@router.post('/predict_health_risk/')

async def predict_risk(user_data:dict):
    return await predict_health_risk(user_data)

