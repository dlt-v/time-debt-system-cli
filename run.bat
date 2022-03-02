@echo off
mode con: cols=80 lines=15
CALL G:\dev\time-debt-system-cli\venv\Scripts\activate.bat
Z:\Python\python.exe G:\dev\time-debt-system-cli\main.py
pause