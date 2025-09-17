# backend/app.py
import os, json, re
from fastapi import FastAPI
from pydantic import BaseModel
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class Query(BaseModel):
    text: str

PROMPT_TEMPLATE = """You are an expert career advisor.
Input: {input}
Return JSON only using this schema:
{"summary":"", "career_paths":[...], "skills":[...], "learning_resources":[...], "action_plan":[...]}
"""

@app.post("/advise")
async def advise(q: Query):
    prompt = PROMPT_TEMPLATE.format(input=q.text)
    resp = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=600,
        temperature=0.6
    )
    raw = resp.choices[0].message.content.strip()
    try:
        return json.loads(raw)
    except Exception:
        m = re.search(r"\{.*\}", raw, re.S)
        return json.loads(m.group(0)) if m else {"error": "could not parse model output", "raw": raw}
