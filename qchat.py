from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables
from db import insert_chat_history
import streamlit as st

import os
from app import *
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemini Pro model and get repsonses
model=genai.GenerativeModel("gemini-pro") 
chat = model.start_chat(history=[])
print(type(chat))
def get_gemini_response(question):
    
    response=chat.send_message(question,stream=True)
    return response

##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")

if submit and input:
    response=get_gemini_response(input)
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The Response is")
    # Save the response to the database
    response_text = ""
    for chunk in response:
        st.write(chunk.text)
        response_text += chunk.text
        st.session_state['chat_history'].append(("Bot", chunk.text))
    insert_chat_history(user_input=input, model_response=response_text)
st.subheader("The Chat History is")
    
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")


    




