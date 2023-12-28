from dotenv import load_dotenv
load_dotenv()  # Loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("google api key"))

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro") 
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Initialize session state for chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Initialize the streamlit app
st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

input_text = st.text_input("Input: ", key="input")
submit_button = st.button("Ask the question")

if submit_button and input_text:
    response = get_gemini_response(input_text)
    # Add user query and response to session state chat history
    st.session_state.chat_history.append(("You", input_text))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state.chat_history.append(("Bot", chunk.text))

st.subheader("The Chat History is")
for role, text in st.session_state.chat_history:
    st.write(f"{role}: {text}")
