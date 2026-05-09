from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from core.llm import llm
from core.prompts import QUERY_REWRITE_PROMPT

rewrite_prompt = ChatPromptTemplate.from_template(QUERY_REWRITE_PROMPT)

query_rewriter = rewrite_prompt | llm | StrOutputParser()