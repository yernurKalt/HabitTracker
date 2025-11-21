


from fastapi import HTTPException, status
from app.Habits.schemas import Habit
from app import storage


def get_habit_or_404(habit_id: int) -> Habit:
    for habit in storage.habits.values():
        if habit.id == habit_id:
            return habit
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Habit is not found")