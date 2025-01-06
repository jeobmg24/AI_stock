import streamlit as st
from create_account import check_user #used to verify that the user is in the database

def login_page():
    st.header("Login")
    user = st.text_input("Username", "Input your username")
    password = st.text_input("Password", type="password")
    enter = st.button("Log in")
    creator = st.button("Create Account")

    if enter:
        if user:
            record = check_user(username=user, password=password)
            if record:
                st.session_state.user = user
                st.session_state.logged_in = True
                st.query_params.page = "dashboard"  
                st.rerun()
            else:
                st.error("No user exists with this password and username combo")
        else:
            st.error("Invalid username or password")
    if creator:
        st.session_state.create_account = True
        st.rerun()
        
    
