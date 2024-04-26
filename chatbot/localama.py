from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

## PROMPT TEMPLATE

prompt=ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assitant. Please respond to user queries"),
        ("user", "Question:{question}")
    ]
)

## streamlit framework
st.title("Langchain Demo with Llama2")
input_text = st.text_input("Search the topic u want to know about")

# openAI LLM
llm=Ollama(model="llama2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    output=chain.invoke({'question':input_text})
    st.write(output)
