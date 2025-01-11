from fastapi import FastAPI
from .api import emotion_analysis , health_risk

app = FastAPI()

app.include_router(health_risk.router)
app.include_router(emotion_analysis.router)

