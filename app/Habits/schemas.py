from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class HabitBase(BaseModel):
    name: str
    description: Optional[str] = None
    goal_per_day: int = 1


class HabitCreate(HabitBase):
    pass


class Habit(HabitBase):
    id: int
    created_at: datetime
    is_active: bool = True

    class Config:
        orm_mode = True