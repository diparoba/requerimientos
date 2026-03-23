from pydantic import BaseModel
from typing import Optional

class ExerciseBase(BaseModel):
    title: str
    description: str
    video_url: Optional[str] = None

class Exercise(ExerciseBase):
    id: int

    class Config:
        orm_mode = True

class TreatmentBase(BaseModel):
    name: str
    description: str

class Treatment(TreatmentBase):
    id: int

    class Config:
        orm_mode = True
