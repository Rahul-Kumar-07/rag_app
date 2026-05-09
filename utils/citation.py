def build_citations(docs):

    citations = []

    for doc in docs:

        source = doc.metadata.get(
            "source",
            "Unknown"
        )

        page = doc.metadata.get(
            "page",
            "N/A"
        )

        citations.append(
            f"{source} (Page {page})"
        )

    return list(set(citations))