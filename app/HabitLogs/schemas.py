from pydantic import BaseModel, ConfigDict
from datetime import date


class HabitLogBase(BaseModel):
    date: date
    count: int = 1


class HabitLogCreate(HabitLogBase):
    pass


class HabitLog(HabitLogBase):
    id: int
    habit_id: int
    
    model_config = ConfigDict(from_attributes=True)