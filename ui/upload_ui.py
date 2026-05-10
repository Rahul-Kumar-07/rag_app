import tempfile
import time

import streamlit as st

from ingestion.ingest import (
    ingest_file
)

def render_upload_ui(
    user_id
):

    st.subheader(
        "📂 Upload Documents"
    )

    # -----------------------------------
    # Session States
    # -----------------------------------

    if "processing_docs" not in st.session_state:

        st.session_state.processing_docs = False

    if "upload_success" not in st.session_state:

        st.session_state.upload_success = False

    if "upload_message" not in st.session_state:

        st.session_state.upload_message = ""

    # -----------------------------------
    # Success Message
    # -----------------------------------

    if st.session_state.upload_success:

        st.success(
            st.session_state.upload_message
        )

    # -----------------------------------
    # File Upload
    # -----------------------------------

    uploaded_files = st.file_uploader(

        "Upload PDF, DOCX, CSV, TXT, Images",

        accept_multiple_files=True,

        key="file_uploader"
    )

    # -----------------------------------
    # Disable Button While Processing
    # -----------------------------------

    process_button = st.button(

        "🚀 Process Documents",

        disabled=(
            st.session_state.processing_docs
        ),

        use_container_width=True
    )

    # -----------------------------------
    # Processing Starts
    # -----------------------------------

    if process_button:

        if not uploaded_files:

            st.warning(
                "Please upload at least one file."
            )

            return

        # -----------------------------
        # Disable Button Immediately
        # -----------------------------

        st.session_state.processing_docs = True

        st.rerun()

    # -----------------------------------
    # Actual Processing
    # -----------------------------------

    if (

        st.session_state.processing_docs

        and

        uploaded_files
    ):

        progress_bar = st.progress(0)

        status_text = st.empty()

        total_chunks = 0

        total_files = len(uploaded_files)

        for index, uploaded_file in enumerate(uploaded_files):

            status_text.info(

                f"Processing {uploaded_file.name}"
            )

            extension = (
                uploaded_file.name
                .split(".")[-1]
            )

            with tempfile.NamedTemporaryFile(

                delete=False,

                suffix=f".{extension}"

            ) as tmp:

                tmp.write(
                    uploaded_file.read()
                )

                path = tmp.name

            count = ingest_file(

                path,

                user_id
            )

            total_chunks += count

            progress = int(

                ((index + 1) / total_files) * 100
            )

            progress_bar.progress(progress)

        # -----------------------------------
        # Processing Finished
        # -----------------------------------

        st.session_state.docs_uploaded = True

        st.session_state.processing_docs = False

        st.session_state.upload_success = True

        st.session_state.upload_message = (

            f"""
            ✅ Successfully processed
            {total_files} files
            and ingested
            {total_chunks} chunks
            """
        )

        status_text.success(
            "✅ Processing completed"
        )

        progress_bar.progress(100)

        # Let user SEE success message
        time.sleep(2)

        st.rerun()