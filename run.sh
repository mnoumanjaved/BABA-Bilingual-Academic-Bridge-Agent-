#!/bin/bash
# BABA Quick Run Script for Mac/Linux
# This script will start the BABA application

echo "================================"
echo "Starting BABA Application"
echo "================================"
echo ""

# Check if virtual environment exists
if [ -d "venv" ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
fi

# Check if dependencies are installed
python -c "import streamlit" 2>/dev/null
if [ $? -ne 0 ]; then
    echo ""
    echo "ERROR: Dependencies not installed!"
    echo "Installing dependencies..."
    pip install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo ""
        echo "Failed to install dependencies."
        echo "Please run: pip install -r requirements.txt"
        exit 1
    fi
fi

# Check if .env file has API key
if grep -q "your_openai_api_key_here" .env 2>/dev/null; then
    echo ""
    echo "WARNING: OpenAI API key not configured!"
    echo "Please edit .env file and add your API key."
    echo ""
    read -p "Press Enter to continue anyway or Ctrl+C to exit..."
fi

# Start the application
echo ""
echo "Starting Streamlit server..."
echo "Your browser will open automatically."
echo "Press Ctrl+C to stop the server."
echo ""

streamlit run app.py
