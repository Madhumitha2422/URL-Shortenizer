@echo off

echo Creating a virtual environment...
python -m venv venv

if errorlevel 1 (
    echo Failed to create a virtual environment.
    exit /b 1
)

echo Virtual environment created successfully.

echo Activating virtual environment...
call venv\Scripts\activate

if errorlevel 1 (
    echo Failed to activate virtual environment.
    exit /b 1
)

echo Virtual environment activated successfully.

echo Installing requirements...
pip install -r requirements.txt

if errorlevel 1 (
    echo Failed to install requirements.
    exit /b 1
)

echo Requirements installed successfully.

echo Running Flask application...
python app.py

if errorlevel 1 (
    echo Failed to run Flask application.
    exit /b 1
)

echo Flask application is running.
