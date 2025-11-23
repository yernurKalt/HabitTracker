# Habit tracker web application
### this web application is a pet project created for portfolio.
## **Short description**
### The purpose of this project is to track habits and add notes of completion of habits every day.
### To make it easier for this project, streak system was created.
### User can create a habit, delete, archieve, and track habits.
# Installation 
### Create a directory with the project
``` 
cd <YOUR PATH> 
git clone https://github.com/yernurKalt/HabitTracker.git
```
### Open the directory with project, and create virtual environemnt using
```
python 3 -m venv venv
source <YOUR PATH>HabitTracker/venv/bin/activate
```
### Install libraries 
```
pip install -r requirements.txt
```
### Run server
```
uvicorn app.main:app --reload
```