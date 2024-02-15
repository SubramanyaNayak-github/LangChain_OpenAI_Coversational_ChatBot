import streamlit as st 
import os
from langchain.schema import HumanMessage,SystemMessage,AIMessage
from langchain_community.chat_models.openai import ChatOpenAI



from dotenv import load_dotenv
load_dotenv()



## Initialize Streamlit application

st.set_page_config(page_title = 'Conversational ChatBot')
st.header("Let's chat")


llm = ChatOpenAI(temperature = 0.7)


if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[
        SystemMessage(content="You are a helpful chatbot for Q&A. Your task is to provide informative and relevant answers to users questions.")
        ]

## to get openai response

def get_openai_response(question):

    st.session_state['chat_history'].append(HumanMessage(content=question))
    answer = llm(st.session_state['chat_history'])
    st.session_state['chat_history'].append(AIMessage(question=answer.content))
    return answer.content



input =st.text_input('Input: ',key='input')
response = get_openai_response(input)

submit = st.button('Ask Question')


if submit:
    st.subheader("The Response is")
    st.write(response)
