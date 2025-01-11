from pydantic import BaseModel

class HealthRiskData(BaseModel):
    age: int
    gender: str
    activity_level: str
    diet: str
    pre_existing_conditions: list  # keep the plural form