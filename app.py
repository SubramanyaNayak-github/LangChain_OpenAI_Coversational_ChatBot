import streamlit as st 
import os
from langchain.schema import HumanMessage,SystemMessage,AIMessage
from langchain_community.chat_models.openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory



from dotenv import load_dotenv
load_dotenv()



## Initialize Streamlit application

st.set_page_config(page_title = 'Conversational ChatBot')
st.header("Let's chat")

memory = ConversationBufferMemory(input_key='input', memory_key='conversation_history')


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
    memory.push(st.session_state['chat_history'])
    return answer.content



## To see Stored Message 

'''
# Get all stored messages from memory
stored_messages = memory.get_all()

# Print the stored messages
for message in stored_messages:
    print(message.content)
'''


input =st.text_input('Input: ',key='input')
response = get_openai_response(input)

submit = st.button('Ask Question')


if submit:
    st.subheader("The Response is")
    st.write(response)
