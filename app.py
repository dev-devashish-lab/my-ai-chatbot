import streamlit as st
import os
from google import genai

# Streamlit Secrets se API key load karein

    if "GEMINI_API_KEY" in st.secrets:
    os.environ["GEMINI_API_KEY"] = st.secrets["GEMINI_API_KEY"]

client = genai.Client()

# Web page ka look set karein
st.set_page_config(page_title="Real Estate AI Assistant", page_icon="🏢")
st.title("🏢 Premium Real Estate AI Agent")
st.write("Welcome! I can help you find your dream property or capture premium buyer leads 24/7.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_input := st.chat_input("Ask about properties or type your budget..."):
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        
        # Ekdam sahi formatting wala Gemini API call
        response = client.models.generate_content(
            model='gemini-1.5-flash',
            contents=user_input,
            config={
                'system_instruction': (
                    "You are a premium, ultra-professional Real Estate Sales Agent for a luxury property agency. "
                    "Your main goal is to help clients and politely capture their Name, Phone Number, Budget, and Preferred Location. "
                    "Always sound sophisticated, highly helpful, and executive. Speak strictly in English."
                )
            }
        )
        
        ai_response = response.text
        response_placeholder.markdown(ai_response)
        
    st.session_state.messages.append({"role": "assistant", "content": ai_response})