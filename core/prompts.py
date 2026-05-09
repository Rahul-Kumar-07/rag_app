RAG_PROMPT = """
You are an advanced AI assistant.

Use ONLY the provided context.

If answer is not in context, say:
"I could not find that information."

Context:
{context}

Question:
{question}
"""