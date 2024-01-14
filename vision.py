from dotenv import load_dotenv
load_dotenv() #le todas variaveis do ambiente
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-pro-vision")
#ler modelo gemini e gerar respostas
image=''

def get_gemini_responses(input,image):
    if input!='':
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)

    return response.text
    """ for chunk in response:
        return chunk.text """

st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")
input=st.text_input('escreva alguma coisa',key='input',placeholder='escreva aqui...')
col1,col2=st.columns(2)
with col1:
    upload_file=st.file_uploader('Selecione uma imagem',type=['jpg','png','jpeg'])
with col2:

    if upload_file is not None:
        image=Image.open(upload_file)
        st.image(image,caption="Uploaded Image",use_column_width=True)

submit=st.button('enviar')
if submit:
    response=get_gemini_responses(input,image)
    st.subheader('Resposta: ')
    st.write(response)
