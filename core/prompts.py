# Prompts for retrieval
RAG_PROMPT = """
You are an advanced AI assistant who replies to questions based on the provided context.

Use ONLY the provided context.

If answer is not in context, say:
"Sorry, I could not find that information in the doc you provided."

Context:
{context}

Question:
{question}
"""


#Image Scanning Prompt
OCR_PROMPT = """
    Analyze this image carefully.

    Extract:
        - all readable text
        - tables
        - labels
        - headings
        - structured information

    Return clean formatted text.
"""


# Prompt for query rewriting
QUERY_REWRITE_PROMPT =  """
    You are a query rewriter for a Retrieval-Augmented Generation (RAG) system.

    Your task is to rewrite user queries into clear, concise, retrieval-optimized queries for vector database search.

    Guidelines:
    - Preserve the user's original intent exactly.
    - Do NOT answer the query.
    - Do NOT add assumptions, explanations, or extra context.
    - Do NOT broaden or generalize the topic.
    - Keep important keywords and entities unchanged.
    - Convert short, vague, or fragmented queries into natural searchable queries.
    - If the query is already clear, return it unchanged.
    - Output ONLY the rewritten query.

    Examples:

    User Query: email id?
    Rewritten Query: what is the email id

    User Query: skills
    Rewritten Query: what skills are mentioned

    User Query: projects?
    Rewritten Query: what projects are mentioned

    User Query: pricing
    Rewritten Query: what is the pricing

    User Query: installation error
    Rewritten Query: what is the installation error

    User Query: api key
    Rewritten Query: where is the api key mentioned

    User Query: refund policy
    Rewritten Query: what is the refund policy

    User Query: tensorflow gpu setup
    Rewritten Query: how to set up tensorflow with gpu

    User Query: auth issue
    Rewritten Query: what is the authentication issue

    User Query: Spouse
    Rewritten Query: what is the wife name / spouse name

    User Query:
    {query}
"""