# backend/app.py
from fastapi import FastAPI
import os
import requests

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Career Advisor Backend is running!"}

@app.get("/career-advice")
def get_advice(skill: str):
    # Simple mock response (without OpenAI)
    return {"advice": f"Based on your skill '{skill}', consider exploring AI, Data Science, or Web Development."}
