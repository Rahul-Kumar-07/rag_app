from core.llm import llm

def rerank(query, docs):

    scored_docs = []

    for doc in docs:

        prompt = f"""
        Rate how relevant this document is
        to the query.

        Query:
        {query}

        Document:
        {doc.page_content}

        Return ONLY a number from 1 to 10.
        """

        try:

            response = llm.invoke(prompt)

            score = float(
                response.content.strip()
            )

        except:

            score = 0

        scored_docs.append(
            (score, doc)
        )

    scored_docs.sort(
        key=lambda x: x[0],
        reverse=True
    )

    reranked_docs = [
        doc
        for _, doc in scored_docs
    ]

    return reranked_docs[:5]