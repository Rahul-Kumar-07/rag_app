from core.llm import llm

def compress_docs( query, docs):

    compressed_docs = []

    for doc in docs:

        prompt = f"""
        You are a context compressor
        for a RAG system.

        Extract ONLY the information
        relevant to answering the query.

        Remove irrelevant details.

        Query:
        {query}

        Document:
        {doc.page_content}
        """

        response = llm.invoke(
            prompt
        )

        compressed_text = (
            response.content
        )

        doc.page_content = (
            compressed_text
        )

        compressed_docs.append(
            doc
        )

    return compressed_docs