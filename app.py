import streamlit as st
import os
from google import genai

# Streamlit Secrets se API key load karein
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    client = genai.Client(api_key=api_key)
except Exception:
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

if user_input := st.chat_input("ask about properties..."):
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        response_placeholder = st.empty()

        response = client.models.generate_content(
            model='gemini-1.5-flash',
            contents=user_input,
            config={
                'system_instruction': "You are a professional Real Estate Sales Agent. Help clients and politely capture their Name, Phone, Budget, and Location. Speak strictly in English."
            }
         )

         ai_response = response.text
         response_placeholder.markdown(ai_response)
     
    st.session_state.messages.append({"role": "assistant", "content": ai_response})