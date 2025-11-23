from typing import List
from fastapi import HTTPException, status
from app.HabitLogs.schemas import HabitLog
from app.Habits.schemas import Habit
from app import storage
from app.helpers.dao import BaseDAO


class HabitDAO(BaseDAO):
    lst = storage.habits


class LogDAO(BaseDAO):
    lst = storage.logs


def create_logs_by_habit_id(habit_id: int):
    logs_by_habit_id: List[HabitLog] = []
    found_habit = HabitDAO.find_by_id_or_404(habit_id)
    for habitLog in storage.logs.values():
        if habitLog.habit_id == habit_id and found_habit.created_at.date() <= habitLog.date:
            logs_by_habit_id.append(habitLog)
    logs_by_habit_id = sorted(logs_by_habit_id, key = lambda log: log.date)
    return logs_by_habit_id