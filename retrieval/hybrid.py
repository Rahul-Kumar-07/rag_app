import re

import streamlit as st

class HybridRetriever:

    def __init__(
        self,
        vectorstore
    ):

        self.vectorstore = vectorstore

    def retrieve(
        self,
        query,
        user_id,
        k=10
    ):

        # ---------------------------------
        # Normalize Query
        # ---------------------------------

        normalized_query = (
            query
            .lower()
            .strip()
        )

        keywords = normalized_query.split()

        # ---------------------------------
        # Vector Search
        # ---------------------------------

        vector_docs = (

            self.vectorstore
            .similarity_search(
                query,
                k=k,
                namespace=user_id
            )
        )

        # ---------------------------------
        # Keyword Boosting
        # ---------------------------------

        boosted_docs = []

        for doc in vector_docs:

            content = (
                doc.page_content.lower()
            )

            score = 0

            # Exact keyword matches
            for keyword in keywords:

                if keyword in content:

                    score += 1

            # ---------------------------------
            # Special Handling
            # ---------------------------------

            # Email Detection
            if any(

                word in normalized_query

                for word in [
                    "email",
                    "mail"
                ]
            ):

                if re.search(

                    r"[a-zA-Z0-9._%+-]+@"
                    r"[a-zA-Z0-9.-]+\."
                    r"[a-zA-Z]{2,}",

                    content
                ):

                    score += 10

            # Phone Detection
            if any(

                word in normalized_query

                for word in [
                    "phone",
                    "mobile",
                    "contact"
                ]
            ):

                if re.search(

                    r"(\+?\d[\d\s\-]{8,})",

                    content
                ):

                    score += 10

            # LinkedIn / GitHub
            if any(

                word in normalized_query

                for word in [
                    "linkedin",
                    "github"
                ]
            ):

                if (

                    "linkedin" in content
                    or
                    "github" in content
                ):

                    score += 10

            # Name Queries
            if "name" in normalized_query:

                if any(

                    token in content

                    for token in [

                        "name",

                        "email",

                        "mobile"
                    ]
                ):

                    score += 5

            boosted_docs.append(
                (score, doc)
            )

        # ---------------------------------
        # Sort By Boost Score
        # ---------------------------------

        boosted_docs.sort(

            key=lambda x: x[0],

            reverse=True
        )

        # ---------------------------------
        # Deduplicate
        # ---------------------------------

        final_docs = []

        seen = set()

        for _, doc in boosted_docs:

            content = (
                doc.page_content.strip()
            )

            if content not in seen:

                final_docs.append(doc)

                seen.add(content)

        # ---------------------------------
        # Debug Logs
        # ---------------------------------

        # print("\n\nRETRIEVED DOCS:\n")

        # for doc in final_docs[:k]:

        #     print(doc.page_content[:1000])

        #     print(
        #         "\n-------------------\n"
        #     )

        return final_docs[:k]

# ---------------------------------
# Cached Retriever
# ---------------------------------

@st.cache_resource
def get_hybrid_retriever(
    vectorstore
):

    return HybridRetriever(
        vectorstore
    )