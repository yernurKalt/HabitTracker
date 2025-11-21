from fastapi import FastAPI
from app.routers.create_habit import router as create_habit_router
from app.routers.habit_logs import router as logs_router


app = FastAPI()

app.include_router(create_habit_router)
app.include_router(logs_router)