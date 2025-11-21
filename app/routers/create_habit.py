from datetime import datetime, timezone
from typing import List
from fastapi import APIRouter
from app import storage
from app.Habits.schemas import Habit
from app.helpers.helpers import get_habit_or_404


router = APIRouter(
    prefix="/habits",
    tags=["Create a new habit"]
    )


@router.post("/create")
def create_new_habit(name: str, description: str | None = None, goal_per_day: int = 1) -> Habit:
    habit_id = storage.habit_id_counter
    habit = Habit(
        name=name,
        description=description,
        goal_per_day=goal_per_day,
        id = habit_id,
        created_at=datetime.now(timezone.utc),
        )
    storage.habit_id_counter += 1
    storage.habits[habit.id] = habit
    return habit
    
@router.get("/get/all")
def get_all_habits(is_active: bool | None = None) -> List[Habit]:
    if is_active is None:
        return storage.habits.values()
    elif is_active is True:
        active_habits: List[Habit] = []
        for habit in storage.habits.values():
            if habit.is_active:
                active_habits.append(habit)
        return active_habits
    elif is_active is False:
        not_active_habits: List[Habit] = []
        for habit in storage.habits.values():
            if not habit.is_active:
                not_active_habits.append(habit)
        return not_active_habits
    
@router.get("/get/{id}")
def get_habit_by_id(id: int) -> Habit:
    return get_habit_or_404(id)
        
@router.put("/update/{id}")
def update_habit(id: int, name: str | None = None, description: str | None = None, goal_per_day: int | None = None) -> Habit:
    habit = get_habit_or_404(id)
    habit.name = name
    habit.description = description
    habit.goal_per_day = goal_per_day
    return habit

@router.patch("/{id}/archieve")
def deactivate_habit(id: int) -> Habit:
    habit = get_habit_or_404(id)
    habit.is_active = False
    return habit

@router.delete("/delete/{id}")
def delete_habit(id: int):
    habit = get_habit_or_404(id)
    return storage.habits.pop(habit.id)