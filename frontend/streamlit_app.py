# frontend/streamlit_app.py
import streamlit as st
import requests

st.title("🎓 Personalized Career & Skills Advisor")
st.write("Enter your skill below to get AI-powered career advice:")

skill = st.text_input("Your Skill", "")

if st.button("Get Advice"):
    if skill.strip():
        try:
            backend_url = "https://career-advisor-backend.onrender.com/career-advice"
            response = requests.get(backend_url, params={"skill": skill})
            if response.status_code == 200:
                st.success(response.json()["advice"])
            else:
                st.error("Error fetching advice. Please try again.")
        except Exception as e:
            st.error(f"Failed to connect to backend: {e}")
    else:
        st.warning("Please enter a skill before clicking the button.")
