# backend/app.py
from fastapi import FastAPI
import os
from openai import OpenAI

app = FastAPI()

# Load API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

@app.get("/")
def root():
    return {"message": "Career Advisor Backend is running!"}

@app.get("/career-advice")
def get_career_advice(skill: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful career advisor."},
            {"role": "user", "content": f"Suggest 3 career paths for someone skilled in {skill}."}
        ]
    )
    return {"advice": response.choices[0].message["content"]}
