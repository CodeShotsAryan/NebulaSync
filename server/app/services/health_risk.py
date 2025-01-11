from ..models.health_risk_model import health_risk_model

def predict_health_risk(data):
    # Mock logic: if age > 40 and activity level is low, high risk
    if data.age > 40 and data.activity_level == "low":
        prediction = {"risk": "High", "recommendations": ["Exercise daily", "Consult a doctor"]}
    else:
        prediction = {"risk": "Low", "recommendations": ["Maintain current routine"]}
    return prediction