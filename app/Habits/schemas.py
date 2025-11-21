from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict


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

    model_config = ConfigDict(from_attributes=True)