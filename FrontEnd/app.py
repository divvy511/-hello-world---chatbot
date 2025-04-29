import streamlit as st
import requests

st.title("Chatbot 🤖")

user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input.strip() != "":
        response = requests.post(
            "http://localhost:8000/chat",
            json={"user_input": user_input}
        )

        if response.status_code == 200:
            bot_response = response.json().get("response", "")
            st.text_area("Bot:", value=bot_response, height=200)
        else:
            st.error(f"Error: {response.status_code} — {response.text}")
