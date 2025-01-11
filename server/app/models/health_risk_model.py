from transformers import pipeline

health_risk_model = pipeline('text-classification',model='bert-base-uncased')

def predict(text:str):
    return health_risk_model(text)


