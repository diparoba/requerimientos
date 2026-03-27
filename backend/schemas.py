from pydantic import BaseModel
from typing import Optional

class ExerciseBase(BaseModel):
    title: str
    description: str
    video_url: Optional[str] = None
    image_url: Optional[str] = None


class Exercise(ExerciseBase):
    id: int

    model_config = {
        "from_attributes": True
    }

class TreatmentBase(BaseModel):
    name: str
    description: str

class Treatment(TreatmentBase):
    id: int

    model_config = {
        "from_attributes": True
    }
