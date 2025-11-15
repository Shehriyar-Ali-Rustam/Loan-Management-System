# 💰 Tajiran Brep Tanzeem Calculator - Offline Setup Guide

This guide will help you run this Loan & Profit Calculator application **completely offline** on any computer.

## 📋 Prerequisites

Your friend's computer needs to have **Python 3.8 or higher** installed. That's it!

### Check if Python is installed:
```bash
python --version
```
or
```bash
python3 --version
```

If Python is not installed, download it from: https://www.python.org/downloads/

## 📦 What to Send to Your Friend

Send your friend the entire `Loan-Management-System` folder containing:
- `lms_app.py` - The main application
- `requirements.txt` - Dependencies list
- `run.bat` (for Windows) or `run.sh` (for Linux/Mac) - Easy run scripts
- This guide

## 🚀 Installation Steps

### For Windows Users:

1. **Extract the folder** to any location (e.g., Desktop, Documents)

2. **Open Command Prompt** in the folder:
   - Navigate to the folder
   - Hold Shift + Right-click in the folder
   - Select "Open PowerShell window here" or "Open Command Prompt here"

3. **Create a virtual environment** (one-time setup):
   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment**:
   ```bash
   venv\Scripts\activate
   ```

5. **Install required packages** (one-time setup):
   ```bash
   pip install -r requirements.txt
   ```

6. **Run the application**:
   ```bash
   streamlit run lms_app.py
   ```

   Or simply **double-click** `run.bat`

### For Linux/Mac Users:

1. **Extract the folder** to any location

2. **Open Terminal** in the folder

3. **Create a virtual environment** (one-time setup):
   ```bash
   python3 -m venv venv
   ```

4. **Activate the virtual environment**:
   ```bash
   source venv/bin/activate
   ```

5. **Install required packages** (one-time setup):
   ```bash
   pip install -r requirements.txt
   ```

6. **Run the application**:
   ```bash
   streamlit run lms_app.py
   ```

   Or make the run script executable and run it:
   ```bash
   chmod +x run.sh
   ./run.sh
   ```

## 🌐 Accessing the Application

Once running, the application will automatically open in your default web browser at:
- **http://localhost:8501**

If it doesn't open automatically, just copy the URL from the terminal and paste it into any web browser.

## 🎯 Features

The calculator provides two main functions:

1. **📊 Profit Sharing**
   - Calculate profit distribution based on contributions
   - Enter total amount, member contribution, and profit percentage
   - Get instant calculation of profit shares

2. **💸 Loan Return Calculator**
   - Calculate total repayment amount with interest
   - Enter loan amount and interest percentage
   - Get instant calculation of total return amount

## ⚠️ Important Notes

- **Internet is NOT required** to run the application after initial setup
- The virtual environment (venv folder) keeps everything isolated
- The application runs on your **local computer only**
- No data is sent to the internet
- Works completely offline forever!

## 🛑 Stopping the Application

To stop the application:
- Press `Ctrl + C` in the terminal/command prompt

## 🔄 Running Again Later

After the first-time setup, you only need to:

**Windows:**
```bash
venv\Scripts\activate
streamlit run lms_app.py
```
Or just double-click `run.bat`

**Linux/Mac:**
```bash
source venv/bin/activate
streamlit run lms_app.py
```
Or run `./run.sh`

## 🆘 Troubleshooting

### "Python is not recognized"
- Install Python from https://www.python.org/downloads/
- Make sure to check "Add Python to PATH" during installation

### "streamlit: command not found"
- Make sure virtual environment is activated (you should see `(venv)` in your terminal)
- Try reinstalling: `pip install -r requirements.txt`

### Application won't start
- Check if port 8501 is already in use
- Try closing other applications and run again

### Need help?
- Make sure all files are in the same folder
- Check that Python version is 3.8 or higher
- Ensure virtual environment is activated before running

## 📝 License

Free to use for personal and commercial purposes.
