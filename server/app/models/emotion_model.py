from transformers import pipeline

emotion_model = pipeline('text-classification',model='roberta-base')

def predict(text:str):
    emotion_model(text)
    