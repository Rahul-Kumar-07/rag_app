from langchain_core.prompts import ChatPromptTemplate
from core.llm import llm

rewrite_prompt = ChatPromptTemplate.from_template("""
Rewrite the user query into a standalone,
search optimized query.

Query:
{query}
""")

query_rewriter = rewrite_prompt | llm