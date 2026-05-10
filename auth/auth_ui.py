import re

import streamlit as st

from supabase_conn.supabase_client import (
    supabase
)

# -----------------------------------
# Validators
# -----------------------------------

def is_valid_email(email):

    pattern = (
        r"^[a-zA-Z0-9._%+-]+@"
        r"[a-zA-Z0-9.-]+\."
        r"[a-zA-Z]{2,}$"
    )

    return re.match(
        pattern,
        email
    )

def is_strong_password(password):

    return (

        len(password) >= 8

        and

        re.search(r"[A-Z]", password)

        and

        re.search(r"[a-z]", password)

        and

        re.search(r"\d", password)
    )

# -----------------------------------
# Auth UI
# -----------------------------------

def render_auth():

    # -----------------------------------
    # Custom CSS
    # -----------------------------------

    st.markdown(
        """
        <style>

        .auth-container {

            background: rgba(255,255,255,0.05);

            padding: 2rem;

            border-radius: 24px;

            backdrop-filter: blur(18px);

            border: 1px solid rgba(255,255,255,0.1);

            max-width: 480px;

            margin: auto;

            margin-top: 5vh;

            box-shadow:
                0 8px 32px rgba(0,0,0,0.3);
        }

        .auth-title {

            text-align: center;

            font-size: 2.2rem;

            font-weight: 700;

            margin-bottom: 0.3rem;
        }

        .auth-subtitle {

            text-align: center;

            color: #9ca3af;

            margin-bottom: 2rem;
        }

        .stTextInput > div > div {

            border-radius: 14px;
        }

        .stButton button {

            width: 100%;

            border-radius: 14px;

            height: 3rem;

            font-weight: 600;

            font-size: 1rem;
        }

        </style>
        """,

        unsafe_allow_html=True
    )

    # -----------------------------------
    # Layout
    # -----------------------------------

    left, center, right = st.columns([1,2,1])

    with center:

        st.markdown(
            """
            <div class="auth-container">

            <div class="auth-title">
                📚 Advanced RAG
            </div>

            <div class="auth-subtitle">
                Secure AI-Powered Document Intelligence
            </div>

            </div>
            """,

            unsafe_allow_html=True
        )

        auth_mode = st.radio(

            "Choose Mode",

            ["Login", "Signup"],

            horizontal=True
        )

        email = st.text_input(
            "Email Address"
        )

        password = st.text_input(

            "Password",

            type="password"
        )

        # -----------------------------------
        # Signup
        # -----------------------------------

        if auth_mode == "Signup":

            confirm_password = st.text_input(

                "Confirm Password",

                type="password"
            )

            if st.button(
                "Create Account"
            ):

                # -------------------------
                # Email Validation
                # -------------------------

                if not is_valid_email(email):

                    st.error(
                        "Invalid email format"
                    )

                    return

                # -------------------------
                # Password Validation
                # -------------------------

                if not is_strong_password(password):

                    st.error(
                        """
Password must contain:

• Minimum 8 characters
• One uppercase letter
• One lowercase letter
• One number
                        """
                    )

                    return

                # -------------------------
                # Confirm Password
                # -------------------------

                if password != confirm_password:

                    st.error(
                        "Passwords do not match"
                    )

                    return

                # -------------------------
                # Signup
                # -------------------------

                try:

                    supabase.auth.sign_up({

                        "email": email,

                        "password": password
                    })

                    st.success(
                        """
✅ Account created successfully.

Please check your email
and confirm your account
before logging in.
                        """
                    )

                except Exception as e:

                    st.error(str(e))

        # -----------------------------------
        # Login
        # -----------------------------------

        else:

            if st.button(
                "Login"
            ):

                if not is_valid_email(email):

                    st.error(
                        "Invalid email format"
                    )

                    return

                if not password:

                    st.error(
                        "Password required"
                    )

                    return

                try:

                    response = (

                        supabase
                        .auth
                        .sign_in_with_password({

                            "email": email,

                            "password": password
                        })
                    )

                    st.session_state.user = (
                        response.user
                    )

                    st.success(
                        "Login successful"
                    )

                    st.rerun()

                except Exception:

                    st.error(
                        """
Invalid credentials
or email not verified.
                        """
                    )