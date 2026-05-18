:: this is a batch a file used to execute command written in this file into the terminal. 
::---

:: Prevents printing command line
@echo off

:: Creates a virtual environment in the .venv folder
python -m venv discord-bot/python/venv/.venv

:: Activates venv
.venv\Scripts\activate

:: Deactivates venv
deactivate