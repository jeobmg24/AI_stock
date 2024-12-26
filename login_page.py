import streamlit as st

def login_page():
    st.header("Login")
    user = st.text_input("Username", "Input your username")
    password = st.text_input("Password", type="password")
    enter = st.button("Log in")

    if enter:
        if user:
            st.session_state.user = user
            st.session_state.logged_in = True
            st.query_params.page = "dashboard"  
            st.rerun()
        else:
            st.error("Invalid username or password")
