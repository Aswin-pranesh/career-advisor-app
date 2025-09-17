# 🚀 Render Deployment Guide for Career Advisor Project

## 1. Backend (FastAPI)
1. Go to Render → New → Web Service
2. Connect to your GitHub repo
3. Set configuration:
   - Name: `career-advisor-backend`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn app:app --host 0.0.0.0 --port $PORT`
4. Attach Environment Group:
   - `OPENAI_API_KEY = your_key_here`
5. Deploy and test:
   - Visit `/` → should return `{"message": "Career Advisor Backend is running!"}`
   - Visit `/career-advice?skill=python` → should return advice.

## 2. Frontend (Streamlit)
1. Go to Render → New → Web Service
2. Connect the same GitHub repo
3. Root directory = where `streamlit_app.py` is
4. Set configuration:
   - Name: `career-advisor-frontend`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `streamlit run streamlit_app.py --server.port $PORT --server.headless true`
5. Attach same Environment Group if needed.
6. Deploy and open the frontend URL.

✅ Done! You now have a backend + frontend running on Render.
