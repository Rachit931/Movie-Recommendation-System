## Movie Recommendation System

A scalable movie recommendation system built using collaborative filtering techniques.

The project implements a full machine learning pipeline including data preprocessing, similarity computation, recommendation generation, and a deployable web interface.

---

## Features

• Movie recommendation engine  
• Collaborative filtering model  
• FastAPI inference API  
• Streamlit web interface  
• Movie posters via TMDB API  

---

## Tech Stack

Python  
NumPy  
Pandas  
SciPy  
Scikit-Learn  
FastAPI  
Streamlit  

---

## Project Architecture

User → Streamlit UI → FastAPI API → Recommendation Engine

---

## Project Structure

data/
raw datasets

src/
machine learning pipeline

api/
backend inference server

app/
streamlit frontend

models/
saved models

---

## Running the Project (local)

Start backend:

uvicorn api.main:app --reload

Start frontend:

streamlit run app/streamlit_app.py

---

## Dataset

Netflix Prize Dataset

https://www.kaggle.com/netflix-inc/netflix-prize-data