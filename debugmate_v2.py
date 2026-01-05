import streamlit as st
import google.generativeai as genai
import os

# --- PAGE SETUP ---
st.set_page_config(page_title="DebugMate", page_icon="🐞")

st.title("🐞 DebugMate")
st.subheader("Your AI-Powered Debugging Assistant")

# --- SIDEBAR (API KEY) ---
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Enter Google Gemini API Key", type="password")
    st.info("Get your key from Google AI Studio")

# --- MAIN INPUT ---
st.write("Paste your error log or buggy code below:")
user_input = st.text_area("Error Log / Code", height=200)

# --- LOGIC ---
if st.button("Fix My Bug 🚀"):
    if not api_key:
        st.error("Please enter your API Key in the sidebar first!")
    elif not user_input:
        st.warning("Please paste some code or an error log.")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel("gemini-1.5-pro")
            
            with st.spinner("Analyzing your bug..."):
                prompt = f"You are an expert debugger. Explain this error simply and provide the fixed code:\n\n{user_input}"
                response = model.generate_content(prompt)
            
            st.success("Analysis Complete!")
            st.markdown(response.text)
            
        except Exception as e:
            st.error(f"An error occurred: {e}")
