import streamlit as st

def load_css():

    st.markdown(
        '''
        <style>

        .stApp {

            background: #0f172a;
            color: white;
        }

        #MainMenu {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }

        header {
            visibility: hidden;
        }

        </style>
        ''',

        unsafe_allow_html=True
    )