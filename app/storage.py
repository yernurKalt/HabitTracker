


from typing import List
from app.HabitLogs.schemas import HabitLog
from app.Habits.schemas import Habit


habits: List[Habit] = []
logs: List[HabitLog] = []
habit_id_counter = 1
log_id_counter = 1