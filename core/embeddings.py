# from langchain_google_genai import (
#     GoogleGenerativeAIEmbeddings
# )

# from core.config import GOOGLE_API_KEY

# embeddings = GoogleGenerativeAIEmbeddings(
#     model="models/embedding-001",
#     google_api_key=GOOGLE_API_KEY,
#     task_type="retrieval_document"
# )

# from langchain_community.embeddings import (
#     HuggingFaceEmbeddings
# )

# embeddings = HuggingFaceEmbeddings(
#     model_name="BAAI/bge-small-en-v1.5"
# )

# from langchain_google_genai import (
#     GoogleGenerativeAIEmbeddings
# )

# embeddings=GoogleGenerativeAIEmbeddings(
#         model="models/gemini-embedding-001"
#           )


import streamlit as st
from langchain_openai import OpenAIEmbeddings

from core.config import OPENAI_API_KEY


# -----------------------------------
# Cached Embedding Model
# -----------------------------------

@st.cache_resource
def get_embeddings():

    return OpenAIEmbeddings(
        model="text-embedding-3-large",
        api_key=OPENAI_API_KEY,
        base_url="https://openrouter.ai/api/v1"
    )

# -----------------------------------
# Shared Embedding Instance
# -----------------------------------

embeddings = get_embeddings()