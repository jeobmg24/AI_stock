import streamlit as st
import yfinance as yf

def get_data():
    stock = st.session_state.tick
    data = yf.Ticker(stock)
    return data.info

def logout():
    st.session_state.logged_in = False
    st.query_params.page = "login"  # Navigate back to login page

def dashboard():
    st.button("Logout", on_click=logout)
    st.header("Dashboard")
    col1, col2 = st.columns([1,1])
    with col1:
        if st.button("Stock sentiment", use_container_width=True):
            st.query_params.page = "sentiment"
            st.rerun()
    with col2:
        if st.button("check Database", use_container_width=True):
            st.query_params.page = "database_screen"
            st.rerun()
    if st.button("Train model (not functional)", use_container_width=True):
        st.query_params.page = "stock_analysis"  # Switch to stock analysis page
        st.rerun()

    tick = st.text_input("What stock would you like to track", value=None, key="tick")
    if tick:
        st.write("The stock you have chosen is:", tick)
        data = get_data()
        st.json(data)
    

    
