import streamlit as st
import os
from google import genai
from dotenv import load_dotenv

# .env file se API key load karein
load_dotenv()

# Gemini Client initialize karein
client = genai.Client()

# Web page ka title aur look set karein
st.set_page_config(page_title="AI Business Assistant", page_icon="🤖")
st.title("🤖 AI Business Assistant")
st.write("Welcome! How can I help your business today?")

# Chat history ko yaad rakhne ke liye
if "messages" not in st.session_state:
    st.session_state.messages = []

# Purani baatein screen par dikhane ke liye
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User se input lene ke liye chat box
if user_input := st.chat_input("Type your message here..."):
    # 1. User ka message screen par dikhao
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # 2. Gemini se response lo
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        
        # Latest Gemini API call
        response = client.models.generate_content(
            model='gemini-3.6-flash',
            contents=user_input
        )
        
        ai_response = response.text
        response_placeholder.markdown(ai_response)
        
    # 3. AI ka response history mein save karo
    st.session_state.messages.append({"role": "assistant", "content": ai_response})