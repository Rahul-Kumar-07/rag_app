from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from core.llm import llm
from retrieval.retriever import retriever
from core.prompts import RAG_PROMPT

prompt = ChatPromptTemplate.from_template(RAG_PROMPT)

chain = (
    {
        "context": retriever,
        "question": lambda x: x
    }
    | prompt
    | llm
    | StrOutputParser()
)
