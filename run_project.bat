@echo off
REM ============================================================
REM IoT Analytics + Spark Web UI Project Launcher
REM ============================================================
REM This script starts your complete IoT project with Spark integration

echo.
echo ============================================================
echo IoT Analytics + Spark Web UI - Project Launcher
echo ============================================================
echo.

REM Navigate to project directory
cd /d "c:\spark project"

REM Activate virtual environment and start server
echo Starting Flask server with Spark integration...
echo.

.\.venv\Scripts\python.exe server.py

REM Keep window open if server crashes
if errorlevel 1 (
    echo.
    echo Error starting server. Press any key to exit...
    pause
)
