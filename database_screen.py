import streamlit as st
from db import get_user_records


def show_database():
    if st.button("Back to Dashboard"):
        st.query_params.page = "dashboard"  # Navigate back to dashboard
        st.rerun()
    st.header("See recent history")
    records = get_user_records(st.session_state.user)
    for record in records:
        st.write(f'Stock:{record[0]} Sentiment: {record[1]} Date: {record[2]}')  # Display each record in the database
    