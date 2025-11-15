#!/data/data/com.termux/files/usr/bin/bash

# Termux Setup Script for Tajiran Brep Tanzeem Calculator
# Run this script in Termux to automatically set up the app

echo "╔═══════════════════════════════════════════════════════╗"
echo "║  Tajiran Brep Tanzeem Calculator - Termux Setup      ║"
echo "╚═══════════════════════════════════════════════════════╝"
echo ""

# Update and upgrade packages
echo "📦 Updating Termux packages..."
pkg update -y && pkg upgrade -y

# Install Python
echo ""
echo "🐍 Installing Python..."
pkg install python -y

# Install pip
echo ""
echo "📌 Installing pip..."
pkg install python-pip -y

# Install Streamlit
echo ""
echo "🌊 Installing Streamlit (this may take a few minutes)..."
pip install streamlit

# Create app directory if it doesn't exist
if [ ! -d "LoanCalculator" ]; then
    mkdir -p LoanCalculator
fi

cd LoanCalculator

# Check if lms_app.py exists
if [ ! -f "lms_app.py" ]; then
    echo ""
    echo "⚠️  lms_app.py not found!"
    echo "Please copy lms_app.py to the LoanCalculator folder"
    echo ""
    echo "You can use:"
    echo "  termux-setup-storage"
    echo "  cp ~/storage/downloads/lms_app.py ."
    exit 1
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "To start the calculator, run:"
echo "  cd LoanCalculator"
echo "  streamlit run lms_app.py --server.headless true"
echo ""
echo "Then open your browser to: http://localhost:8501"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
