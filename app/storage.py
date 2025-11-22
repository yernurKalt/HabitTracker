


from datetime import date
from typing import Dict, List
from app.HabitLogs.schemas import HabitLog
from app.Habits.schemas import Habit


habits: Dict[int, Habit] = dict()
logs: Dict[int, HabitLog] = dict()
log_dates_by_habit_id: Dict[int, List[date]] = dict()
habit_id_counter = 1
log_id_counter = 1