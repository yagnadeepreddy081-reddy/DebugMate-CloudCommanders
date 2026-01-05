import streamlit as st
import google.generativeai as genai

# ==========================================
# 1. CONFIGURATION
# ==========================================
# ⚠️ PASTE YOUR KEY HERE
API_KEY = "AIzaSyAIE6xAVgegat5IfvJHjRzI9rSGRrwccf0"

# ------------------------------------------
# AUTO-DETECT WORKING MODEL
# ------------------------------------------
model = None
model_name_to_use = "gemini-pro" # Default fallback

try:
    genai.configure(api_key=API_KEY)
    
    # We ask Google: "What models are allowed for me?"
    found_model = False
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            if 'flash' in m.name:
                model_name_to_use = m.name
                found_model = True
                break
            elif 'gemini-pro' in m.name:
                model_name_to_use = m.name
                found_model = True
    
    # Configure the model with the name we found
    model = genai.GenerativeModel(model_name_to_use)

except Exception as e:
    st.error(f"⚠️ API Key Error: Please check your API key. {e}")

# ==========================================
# 2. UI DESIGN
# ==========================================
st.set_page_config(page_title="DebugMate", page_icon="🐛", layout="wide")

st.title("👨‍🏫 DebugMate: The Anti-Cheat Tutor")
st.caption(f"Connected to AI Model: {model_name_to_use}")

col1, col2 = st.columns(2)
with col1:
    code_input = st.text_area("Paste Code Here (Required):", height=200)
with col2:
    # Changed label to indicate it's optional
    error_input = st.text_area("Paste Error Here (Optional):", height=200) 

# ==========================================
# 3. THE LOGIC
# ==========================================
if st.button("🧠 Guide Me (Tutor Mode)"):
    # MODIFICATION 1: We only check if code_input is missing
    if not code_input:
        st.warning("⚠️ Please paste your code first!")
    else:
        with st.spinner("Analyzing..."):
            try:
                # MODIFICATION 2: Dynamic Prompting
                if error_input:
                    # Scenario A: User gave an error message
                    task_description = f"The student provided this error message: {error_input}"
                else:
                    # Scenario B: No error message provided
                    task_description = "The student did NOT provide an error message. Find potential bugs, logical errors, or typos in the code yourself."

                prompt = f"""
                Act as a strict Lab Professor.
                
                Student Code: 
                {code_input}
                
                Context:
                {task_description}
                
                Instructions:
                1. DO NOT give the fixed code.
                2. If there is an error provided, explain it.
                3. If no error is provided, find the bug and explain why the code fails or behaves unexpectedly.
                4. Point out the line number.
                """
                
                response = model.generate_content(prompt)
                
                st.info("👨‍🏫 Professor says:")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"Error: {e}")