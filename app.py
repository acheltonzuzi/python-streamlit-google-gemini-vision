from dotenv import load_dotenv
load_dotenv() #le todas variaveis do ambiente
import streamlit as st
import os
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-pro")
#ler modelo gemini e gerar respostas

def get_gemini_responses(text):
    response=model.generate_content(text)
    #return response.text
    for chunk in response:
        return chunk.text

st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")
input=st.text_input('escreva alguma coisa',key='input',placeholder='escreva aqui...')
submit=st.button('ask question')
if submit:
    response=get_gemini_responses(input)
    st.subheader('Resposta:')
    st.write(response)