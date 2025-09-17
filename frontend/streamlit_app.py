# frontend/streamlit_app.py
import os, requests
import streamlit as st

BACKEND_URL = os.getenv("BACKEND_URL", "https://your-backend.onrender.com")

st.title("🎯 Personalized Career & Skills Advisor")
user_text = st.text_area("Describe your background & interests:")

if st.button("Get Advice"):
    with st.spinner("Generating..."):
        r = requests.post(f"{BACKEND_URL}/advise", json={"text": user_text}, timeout=60)
        if r.ok:
            data = r.json()
            st.subheader("Summary")
            st.write(data.get("summary"))
            st.subheader("Career paths")
            for p in data.get("career_paths", []):
                st.markdown(f"**{p['title']}** — {p.get('why','')}")
            st.subheader("Action Plan")
            for a in data.get("action_plan", []):
                st.write("-", a)
        else:
            st.error("Backend error: " + r.text)
