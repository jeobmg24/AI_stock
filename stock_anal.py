import streamlit as st
import yfinance as yf
import pandas as pd


def download_stock_info(tickers):
    all_data = {}
    tickers = tickers.split(',')
    print(f'tickers: {tickers}')
    for ticker in tickers:
        ticker = ticker.strip()
        all_data[ticker] = yf.download(ticker, start='2020-01-01')
    return all_data

def merge_into_dataframe(all_data):
    """This function takes all the data (dictionary) from the 'download_stock_info' function 
       and puts it into a single dataFrame"""
    combined_data = {}
    for ticker, data in all_data.items():
        data = data.copy()
        data.columns = [f'{ticker}_{col}' for col in data.columns]
        combined_data[ticker] = data
    
    combined_df = pd.concat(combined_data.values(), axis=1)
    return combined_df
        
       
    
    
def stock_anal():
    st.header("Stock Analysis")
    stocks = st.text_input("Stocks to put into screener (comma-separated)")
    result_area = st.empty()  
    if st.button("Enter"):
            #print(download_stock_info(stocks))
            all_data = download_stock_info(stocks)
            comb_df = merge_into_dataframe(all_data=all_data).head() # this is the dataframe
    
            result_area.write(comb_df.head())
            
            
        
            
    
    # Navigate back to the dashboard
    if st.button("Back to Dashboard"):
        st.query_params.page = "dashboard"  # Navigate back to dashboard
        st.rerun()


if  __name__ == "__main__":
    stock_anal()
    aapl = yf.Ticker("aapl")
    #print(aapl.info)
    print(aapl.eps_trend)
    print(aapl.earnings_history)
