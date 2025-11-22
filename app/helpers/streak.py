from datetime import datetime, date, timedelta
from typing import List



def longest_streak(dates: List):
    streak = 0
    for date in dates:
        diff = date - timedelta(days=1) 
        if diff not in dates:
            length = 1
            while timedelta(days=length) + date in dates:
                length += 1
            streak = max(length, streak)
    return(streak)


def current_streak(dates: List):
    today = date.today()
    streak = 0
    if today == dates[-1]:
        streak = 1
        while today - timedelta(days=streak) in dates:
            streak += 1
    return streak 
