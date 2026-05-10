import streamlit as st

from graph.workflow import graph

def render_chat_ui(
    user_id
):

    st.divider()

    for chat in (
        st.session_state.chat_history
    ):

        if chat["role"] == "user":

            st.markdown(
                f"🧑 **You:** {chat['content']}"
            )

        else:

            st.markdown(
                f"🤖 **Assistant:** {chat['content']}"
            )

    question = st.chat_input(

        "Ask your question...",

        disabled=(
            st.session_state
            .processing_question
        )
    )

    if question:

        st.session_state.processing_question = True

        st.session_state.chat_history.append({

            "role": "user",

            "content": question
        })

        st.markdown(
            f"🧑 **You:** {question}"
        )

        bot_placeholder = st.empty()

        with bot_placeholder.container():

            with st.spinner(
                "🤖 Thinking..."
            ):

                response = graph.invoke({

                    "question": question,

                    "user_id": user_id
                })

        answer = response["answer"]

        st.session_state.chat_history.append({

            "role": "assistant",

            "content": answer
        })

        bot_placeholder.markdown(

            f"🤖 **Assistant:** {answer}"
        )

        st.session_state.processing_question = False

        st.rerun()