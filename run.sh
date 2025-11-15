#!/bin/bash

echo "===================================="
echo "Tajiran Brep Tanzeem Calculator"
echo "===================================="
echo ""

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo ""
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Check if streamlit is installed
python -c "import streamlit" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Installing required packages..."
    pip install -r requirements.txt
    echo ""
fi

# Run the application
echo "Starting Loan Calculator..."
echo ""
echo "The application will open in your browser at http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop the application"
echo ""
python -m streamlit run lms_app.py
