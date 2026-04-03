# Titanic Survival Prediction System (Production-Ready ML Project)

## Overview
This project is a production-grade machine learning system that predicts whether a passenger would survive the Titanic disaster. It is built using a full-stack ML architecture with a clear separation between backend and frontend, simulating real-world deployment practices.

---

## Live Application

- Frontend (Streamlit): https://titanicsurvivalpred-fveixm4x6umdf9sx5vgk2y.streamlit.app  
- Backend API Docs (FastAPI): https://titanic-survival-pred.onrender.com/docs  

---

## Key Highlights

- End-to-end ML pipeline (data processing → model training → evaluation → deployment)
- FastAPI backend for serving predictions via REST API
- Streamlit frontend for user interaction
- Production-style deployment using Render and Streamlit Cloud
- Model persistence using joblib
- Clean separation of concerns between services

---

## Architecture

User → Streamlit Frontend → FastAPI Backend → ML Model → Prediction

Backend is served using Gunicorn with Uvicorn workers to simulate a production environment.

---

## Tech Stack

- Python  
- Scikit-learn  
- Pandas, NumPy  
- FastAPI  
- Streamlit  
- Gunicorn + Uvicorn  
- Joblib  

---


## Running Locally

### 1. Clone Repository
git clone <repo-url>  
cd titanic  

### 2. Create Virtual Environment
python -m venv myenv  
source myenv/bin/activate  

### 3. Install Dependencies
pip install -r requirements.txt  

### 4. Run Backend (Development Mode)
uvicorn main:app --reload  

### 5. Run Backend (Production Simulation)
gunicorn -w 2 -k uvicorn.workers.UvicornWorker main:app  

### 6. Run Frontend
streamlit run streamlit_app.py  

---

## Deployment Details

### Backend Deployment (Render)

Build Command:
pip install -r requirements.txt  

Start Command:
gunicorn -w 2 -k uvicorn.workers.UvicornWorker main:app  

### Frontend Deployment (Streamlit Cloud)

- Connected directly to GitHub repository  
- Entry file: streamlit_app.py  

---

## Major Issues Faced and Fixes

### Module Import Error (ModuleNotFoundError: src)
Cause: Python could not locate the src module.  
Fix:  
PYTHONPATH=. uvicorn main:app --reload  

---

### Connection Refused Error
Cause: Streamlit was trying to connect to localhost instead of deployed backend.  
Fix: Updated API URL to use deployed Render endpoint.  

---

### Model Loading Failure
Cause: model.pkl file was not included in deployment.  
Fix: Ensured artifacts directory is committed and pushed to GitHub.  

---

### Gunicorn Worker Boot Failure
Cause: Missing dependencies or incorrect imports.  
Fix: Updated requirements.txt with all necessary packages.  

---

### Feature/Column Mismatch
Cause: Input data did not match training features.  
Fix: Ensured preprocessing pipeline consistency between training and inference.  

---

## Model Performance

- Evaluation Metric: ROC-AUC  
- Score: Approximately 0.85  
- Addressed class imbalance during training  

---

## Key Learnings

- Importance of separating backend and frontend in ML systems  
- Real-world deployment and debugging challenges  
- Handling API-based model serving  
- Managing dependencies and environment consistency  

---

## Future Improvements

- Add input validation using Pydantic  
- Dockerize the application for portability  
- Implement CI/CD pipelines  
- Add monitoring and logging  
- Deploy on cloud infrastructure with reverse proxy (Nginx)  

---

## Author

Prachya Das  

---

## Why This Project Stands Out

This project goes beyond a typical machine learning notebook. It demonstrates:

- Production-oriented system design  
- API development and integration  
- Full-stack ML deployment  
- Real-world debugging and problem solving  

It reflects the mindset and practices expected from a machine learning engineer working on real systems.
