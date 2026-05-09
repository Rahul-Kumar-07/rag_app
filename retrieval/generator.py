from langchain_core.prompts import (
    ChatPromptTemplate
)

from langchain_core.output_parsers import (
    StrOutputParser
)

from core.llm import llm

prompt = ChatPromptTemplate.from_template(
    """
    You are a helpful AI assistant.

    Answer ONLY using
    the provided context.

    Context:
    {context}

    Question:
    {question}
    """
)

generator = (
    prompt
    | llm
    | StrOutputParser()
)

def generate_answer( question, docs):

    context = "\n\n".join([

        d.page_content

        for d in docs
    ])

    return generator.invoke({

        "context": context,

        "question": question
    })