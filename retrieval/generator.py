from langchain_core.prompts import (
    ChatPromptTemplate
)

from langchain_core.output_parsers import (
    StrOutputParser
)

from core.llm import llm
from core.prompts import GENERATOR_PROMPT

prompt = ChatPromptTemplate.from_template(GENERATOR_PROMPT)

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