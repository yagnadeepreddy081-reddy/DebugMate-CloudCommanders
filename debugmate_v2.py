import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="DebugMate", page_icon="🐞")
st.title("🐞 DebugMate")

# Sidebar
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

# Main Input
user_input = st.text_area("Paste Error Log Here:", height=200)

if st.button("Fix Bug"):
    if not api_key:
        st.error("Please enter API Key in sidebar.")
    elif not user_input:
        st.warning("Please enter an error log.")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel("gemini-1.5-pro")
            with st.spinner("Analyzing..."):
                response = model.generate_content(f"Fix this error: {user_input}")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
