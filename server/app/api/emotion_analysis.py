from fastapi import APIRouter
from ..services.emotion_analysis import emotion_analysis
router = APIRouter

@router.post('/analyze_emotion/')
async def emotion_analyze(user_data : dict):
    return await emotion_analysis(user_data)