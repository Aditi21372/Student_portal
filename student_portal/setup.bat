@echo off
echo Setting up Student Portal...

REM Create virtual environment
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Create .env file if it doesn't exist
if not exist ".env" (
    echo Creating .env file from template...
    copy .env.example .env
    echo Please update the .env file with your settings
)

REM Run migrations
echo Running database migrations...
python manage.py migrate

echo Setup complete!
echo To start the server, run: python manage.py runserver
echo The application will be available at http://127.0.0.1:8000/student_api/api/
pause
