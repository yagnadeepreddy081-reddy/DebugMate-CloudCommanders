import streamlit as st
import google.generativeai as genai

st.title("DebugMate")

# Sidebar
api_key = st.sidebar.text_input("Gemini API Key", type="password")

# Main Input
code_input = st.text_area("Paste Error Log")

# Button
if st.button("Fix Bug"):
    # Simple check without nesting
    if not api_key:
        st.error("Please enter API Key")
        st.stop()

    # Configure
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-pro")
    
    # Run
    try:
        response = model.generate_content(f"Fix this: {code_input}")
        st.write(response.text)
    except Exception as e:
        st.error(f"Error: {e}")
