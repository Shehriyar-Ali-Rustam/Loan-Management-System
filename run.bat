@echo off
echo ====================================
echo Tajiran Brep Tanzeem Calculator
echo ====================================
echo.

REM Check if venv exists
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
    echo.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate

REM Check if streamlit is installed
python -c "import streamlit" 2>nul
if errorlevel 1 (
    echo Installing required packages...
    pip install -r requirements.txt
    echo.
)

REM Run the application
echo Starting Loan Calculator...
echo.
echo The application will open in your browser at http://localhost:8501
echo.
echo Press Ctrl+C to stop the application
echo.
streamlit run lms_app.py

pause
