@echo off
REM BABA Quick Run Script for Windows
REM This script will start the BABA application

echo ================================
echo Starting BABA Application
echo ================================
echo.

REM Check if virtual environment exists
if exist "venv\Scripts\activate.bat" (
    echo Activating virtual environment...
    call venv\Scripts\activate.bat
)

REM Check if dependencies are installed
python -c "import streamlit" 2>nul
if errorlevel 1 (
    echo.
    echo ERROR: Dependencies not installed!
    echo Installing dependencies...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo.
        echo Failed to install dependencies.
        echo Please run: pip install -r requirements.txt
        pause
        exit /b 1
    )
)

REM Check if .env file has API key
findstr /C:"your_openai_api_key_here" .env >nul 2>&1
if not errorlevel 1 (
    echo.
    echo WARNING: OpenAI API key not configured!
    echo Please edit .env file and add your API key.
    echo.
    pause
)

REM Start the application
echo.
echo Starting Streamlit server...
echo Your browser will open automatically.
echo Press Ctrl+C to stop the server.
echo.

streamlit run app.py

pause
