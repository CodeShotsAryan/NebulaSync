from ..models.emotion_model import emotion_model

async def analyze_emotion(user_text:str):
    emotion = emotion_model(user_text)
    return {'emotion':emotion}

