from ..models.health_risk_model import health_risk_model

async def predict_health_risk(user_data:dict):
    text = f"Age:{user_data['age']} ,
            Gender:{user_data['gender']},
            Activity Level : {user_data['activity_level']}
            "
    prediction = health_risk_model.predict(text)
    return {'health_risk':prediction}