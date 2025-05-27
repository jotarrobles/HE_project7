# HE_project7
Homomorphic Encryption application for Information Security course

## 🛡️ Healthcare Risk Prediction App

This project contains a simple healthcare risk prediction application using Python, Streamlit, and the `heaan_stat` library for encrypted statistics.

## 📁 Project Structure
HE_project7/
├── app.py # Streamlit application
├── ini.py # Initialization script (run once)
├── requirements.txt
└── README.md # Instructions

## ✅ Prerequisites
- Python 3.8 or newer
- pip (Python package installer)

## 📦 Installation Steps

1. **Clone the repository** (or download this folder manually):
   ```bash
   git clone https://github.com/jotarrobles/HE_project7.git
   cd HE_project7   #comment

2. **(Optional) Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate    #On Windows venv\Scripts\activate
   
3. **Install dependencies**:
   ```bash
    pip install -r requirements.txt

4. **Initialization**:
   Before running the app, you have to run the initialization file once.
   This will setup the keys for the Homomorphic encryption
   ```bash
   python ini.py

5. **Streamlit**:
   Run the app using streamlit
   ```bash
   streamlit run app.py

   The app should open in your default web browser. If not, open a browser window and      search:
   http://localhost:8501

## Inside the app
The first step within the app is to select a CSV file. Within this directory, the file heart_sample.csv is provided for testing.



