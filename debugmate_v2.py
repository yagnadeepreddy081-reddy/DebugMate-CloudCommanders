import streamlit as st
import google.generativeai as genai

st.title("DebugMate")
api_key = st.text_input("Enter API Key", type="password")
user_input = st.text_area("Paste Error Log")

if st.button("Fix Bug"):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(f"Fix this error: {user_input}")
    st.write(response.text)
