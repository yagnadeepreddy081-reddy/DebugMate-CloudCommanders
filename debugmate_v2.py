import streamlit as st
import google.generativeai as genai

# Page Config
st.set_page_config(page_title="DebugMate", page_icon="🐞")
st.title("🐞 DebugMate")
st.write("### AI-Powered Debugging Assistant")

# Sidebar for API Key
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Enter Gemini API Key", type="password")
    st.info("Get your key from Google AI Studio")

# Main Input Area
user_input = st.text_area("Paste your error log or code here:", height=200)

# The Logic
if st.button("Fix My Bug 🚀"):
    if not api_key:
        st.error("Please enter your API Key in the sidebar first!")
    elif not user_input:
        st.warning("Please paste some code/error to analyze.")
    else:
        try:
            # Configure Gemini
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel("gemini-1.5-pro")
            
            with st.spinner("Analyzing..."):
                prompt = f"Fix this error and explain it simply: {user_input}"
                response = model.generate_content(prompt)
            
            st.success("Analysis Complete!")
            st.markdown(response.text)
            
        except Exception as e:
            st.error(f"Error: {e}")
