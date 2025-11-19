from pydantic import BaseModel
from datetime import date


class HabitLogBase(BaseModel):
    date: date
    count: int = 1


class HabitLogCreate(HabitLogBase):
    pass


class HabitLog(HabitLogBase):
    id: int
    habit_id: int
    
    class Config:
        orm_mode = True