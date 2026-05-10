# from langchain_google_genai import ChatGoogleGenerativeAI
# from core.config import GOOGLE_API_KEY

# llm = ChatGoogleGenerativeAI(
#     model="gemini-2.5-flash",
#     google_api_key=GOOGLE_API_KEY,
#     temperature=0.2,
#     # max_output_tokens=2048,
# )

import streamlit as st

from langchain_openai import ChatOpenAI

from core.config import OPENAI_API_KEY

@st.cache_resource
def get_llm():
    return ChatOpenAI(
        model="openai/gpt-4o-mini",
        api_key=OPENAI_API_KEY,
        base_url="https://openrouter.ai/api/v1",
        temperature=0.2
    )

llm = get_llm()