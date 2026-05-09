import re

class HybridRetriever:

    def __init__( self, vectorstore ):
        self.vectorstore = vectorstore
        

    def retrieve(self, query, k=10 ):

        # -----------------------------
        # Vector Search
        # -----------------------------

        vector_docs = (

            self.vectorstore
            .similarity_search(

                query,

                k=k
            )
        )

        # -----------------------------
        # Exact Keyword Boost
        # -----------------------------

        keyword_docs = []

        keywords = query.lower().split()

        for doc in vector_docs:

            content = (
                doc.page_content.lower()
            )

            if any(

                keyword in content

                for keyword in keywords
            ):

                keyword_docs.append(doc)

        # -----------------------------
        # Email Special Handling
        # -----------------------------

        if "email" in query.lower():

            email_pattern = (
                r"[a-zA-Z0-9._%+-]+@"
                r"[a-zA-Z0-9.-]+\."
                r"[a-zA-Z]{2,}"
            )

            for doc in vector_docs:

                if re.search(

                    email_pattern,

                    doc.page_content
                ):

                    keyword_docs.insert(
                        0,
                        doc
                    )

        # -----------------------------
        # Merge Results
        # -----------------------------

        merged = []

        seen = set()

        for doc in (
            keyword_docs + vector_docs
        ):

            content = doc.page_content

            if content not in seen:

                merged.append(doc)

                seen.add(content)

        return merged[:k]