import streamlit as st
import openai
import os

# Set your OpenAI API Key
openai.api_key = st.secrets["openai_api_key"]

st.title("Chat with OpenAI")

# Input text from the user
user_input = st.text_area("Enter your prompt:", "")

if st.button("Generate Response"):
    if user_input:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": user_input}]
            )
            st.write(response["choices"][0]["message"]["content"])
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a prompt.")

