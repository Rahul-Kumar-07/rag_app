import streamlit as st

from core.vectorstore import (
    pinecone_index
)

def get_user_id():

    return (
        st.session_state
        .user
        .id
    )

def user_has_documents(
    user_id
):

    stats = (
        pinecone_index
        .describe_index_stats()
    )

    namespaces = (
        stats.get(
            "namespaces",
            {}
        )
    )

    return user_id in namespaces