from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from core.llm import llm

prompt = ChatPromptTemplate.from_template("""
You are a helpful AI assistant.

Answer ONLY using the provided context.

Context:
{context}

Question:
{question}
""")

generator = (
    prompt
    | llm
    | StrOutputParser()
)

async def generate_answer(question, docs):

    context = "\n\n".join([
        d.page_content
        for d in docs
    ])

    return await generator.ainvoke({
        "context": context,
        "question": question
    })