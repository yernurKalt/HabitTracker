from fastapi import HTTPException, status
from app.HabitLogs.schemas import HabitLog
from app.Habits.schemas import Habit
from app import storage
from app.helpers.dao import BaseDAO


class HabitDAO(BaseDAO):
    lst = storage.habits


class LogDAO(BaseDAO):
    lst = storage.logs
