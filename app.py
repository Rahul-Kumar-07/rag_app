import streamlit as st

from auth.auth_ui import (
    render_auth
)

from auth.auth_utils import (

    get_user_id,

    user_has_documents
)

from ui.upload_ui import (
    render_upload_ui
)

from ui.chat_ui import (
    render_chat_ui
)

from ui.styles import (
    load_css
)

# -----------------------------------
# Page Config
# -----------------------------------

st.set_page_config(

    page_title="Advanced RAG",

    layout="wide"
)

# -----------------------------------
# Styles
# -----------------------------------

load_css()

# -----------------------------------
# Session State
# -----------------------------------

if "docs_uploaded" not in st.session_state:
    st.session_state.docs_uploaded = False


if "upload_processed" not in st.session_state:
    st.session_state.upload_processed = False


if "processing_question" not in st.session_state:
    st.session_state.processing_question = False


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


if "user" not in st.session_state:
    st.session_state.user = None

# -----------------------------------
# Authentication
# -----------------------------------

if not st.session_state.user:

    render_auth()

    st.stop()

# -----------------------------------
# User
# -----------------------------------

user_id = get_user_id()

# -----------------------------------
# Existing Documents
# -----------------------------------

if user_has_documents(user_id):

    st.session_state.docs_uploaded = True

# -----------------------------------
# Header
# -----------------------------------

st.title(
    "📚 Advanced RAG Application"
)

# -----------------------------------
# Sidebar
# -----------------------------------

with st.sidebar:

    st.subheader("Your Workspace")

    render_upload_ui(user_id)

# -----------------------------------
# Chat / Upload
# -----------------------------------

if not st.session_state.docs_uploaded:

    st.info(
        "Upload documents to begin"
    )

else:

    render_chat_ui(user_id)