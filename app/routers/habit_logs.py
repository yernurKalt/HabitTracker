from datetime import date, datetime, timezone
from typing import Dict, List
from fastapi import APIRouter
from app.HabitLogs.schemas import HabitLog
from app.Habits.schemas import Habit
from app.helpers.helpers import HabitDAO, LogDAO
from app import storage


router = APIRouter(
    prefix = "/logs",
    tags=["Logs"]
    )

@router.post("/add")
def add_log(habit_id: int, date: date, count: int):
    habit = HabitDAO.find_by_id_or_404(habit_id)
    log_id = storage.log_id_counter
    habit_log = HabitLog(
        date=date,
        count=count,
        id=log_id,
        habit_id=habit_id,
        )
    storage.log_id_counter += 1
    storage.logs[log_id] = habit_log
    return habit_log

@router.get("/{id}")
def find_logs_by_id(habit_id: int | None = None) -> List[HabitLog]:
    logs_by_habit_id: List[HabitLog] = []
    if habit_id is None:
        logs_by_habit_id = storage.logs.values()
        return logs_by_habit_id
    found_habit = HabitDAO.find_by_id_or_404(habit_id)
    for habitLog in storage.logs.values():
        if habitLog.habit_id == habit_id and found_habit.created_at.date() <= habitLog.date:
            logs_by_habit_id.append(habitLog)
    logs_by_habit_id = sorted(logs_by_habit_id, key = lambda log: log.date)
    only_dates = sorted(set(map(lambda x: x.date, logs_by_habit_id)))
    storage.log_dates_by_habit_id[habit_id] = only_dates
    return logs_by_habit_id
      