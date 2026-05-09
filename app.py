import streamlit as st
import tempfile

from ingestion.ingest import ingest_file
from graph.workflow import graph

# -----------------------------------
# Page Config
# -----------------------------------

st.set_page_config(
    page_title="Advanced RAG",
    layout="wide"
)

st.title("📚 Advanced RAG Application")

# -----------------------------------
# Session State Initialization
# -----------------------------------

if "docs_uploaded" not in st.session_state:
    st.session_state.docs_uploaded = False

if "processing_question" not in st.session_state:
    st.session_state.processing_question = False

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -----------------------------------
# Upload Section
# -----------------------------------

if not st.session_state.docs_uploaded:

    st.subheader("Upload Your Documents")

    uploaded_files = st.file_uploader(
        "Upload PDF, CSV, DOCX, TXT, Images",
        accept_multiple_files=True
    )

    if uploaded_files:

        total_chunks = 0

        for uploaded_file in uploaded_files:

            file_extension = (
                uploaded_file.name
                .split(".")[-1]
            )

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=f".{file_extension}"
            ) as tmp:

                tmp.write(
                    uploaded_file.read()
                )

                path = tmp.name

            with st.spinner(
                f"Processing {uploaded_file.name}..."
            ):

                count = ingest_file(path)

                total_chunks += count

        st.success(
            f"✅ Successfully ingested {total_chunks} chunks"
        )

        st.session_state.docs_uploaded = True

        st.rerun()

# -----------------------------------
# Chat Section
# -----------------------------------

else:

    st.success(
        "✅ Documents uploaded and indexed successfully"
    )

    st.divider()

    # -------------------------------
    # Display Chat History
    # -------------------------------

    for chat in st.session_state.chat_history:

        if chat["role"] == "user":

            st.markdown(
                f"🧑 **You:** {chat['content']}"
            )

        else:

            st.markdown(
                f"🤖 **Assistant:** {chat['content']}"
            )

    # -------------------------------
    # Disable input while processing
    # -------------------------------

    question = st.chat_input(
        "Ask your question...",
        disabled=st.session_state.processing_question
    )

    # -------------------------------
    # User Asked Question
    # -------------------------------

    if question:

        st.session_state.processing_question = True

        # Add user question to history
        st.session_state.chat_history.append({
            "role": "user",
            "content": question
        })

        # Show user question immediately
        st.markdown(
            f"🧑 **You:** {question}"
        )

        # Bot placeholder
        bot_placeholder = st.empty()

        # Spinner beside bot emoji
        with bot_placeholder.container():

            with st.spinner("🤖 Thinking..."):

                response = graph.invoke({
                    "question": question
                })

        answer = response["answer"]

        # Save assistant response
        st.session_state.chat_history.append({
            "role": "assistant",
            "content": answer
        })

        # Replace spinner with answer
        bot_placeholder.markdown(
            f"🤖 **Assistant:** {answer}"
        )

        st.session_state.processing_question = False

        st.rerun()