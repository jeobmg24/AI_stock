import streamlit as st
from db import get_user_records


def show_database():
    if st.button("Back to Dashboard"):
        st.query_params.page = "dashboard"  # Navigate back to dashboard
        st.rerun()
    st.header("See recent history")
    records = get_user_records(st.session_state.user)
    for record in records:
        col1, col2, col3 = st.columns([.4, .3, .3])
        with col1:
            st.write(f'Stock:{record[0]}')
        with col2:
            st.write(f'Sentiment:{record[1]}')
        with col3:
            st.write(f'Date:{record[2]}')
    