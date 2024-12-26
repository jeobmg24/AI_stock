import streamlit as st
from login_page import login_page
from dashboard import dashboard
from stock_anal import stock_anal
from sentiment import show_sentiment
from database_screen import show_database

def main():
    # Initialize session state for logged_in if it doesn't exist
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.user = None

    # Use st.query_params to get the page parameter
    query_params = st.query_params
    page = query_params.get("page", "login")

    # If user is not logged in, show the login page, otherwise show the appropriate page
    if not st.session_state.logged_in:
        login_page()  # Always show the login page when not logged in
    else:
        if page == "dashboard":
            dashboard()  # Display the dashboard if logged in
        elif page == "stock_analysis":
            stock_anal()  # Display the stock analysis page if logged in
        elif page == "sentiment":
            show_sentiment()
        elif page == "database_screen":
            show_database()
        else:
            st.query_params.page = "dashboard"  # Default to dashboard after login

if __name__ == '__main__':
    main()
