import streamlit as st
import yfinance as yf
import joblib
import pandas as pd
from db import insert_sentiment, make_table, get_stock_records

model = joblib.load('sentiment_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

def show_sentiment():
    if st.button("Back to Dashboard"):
        st.query_params.page = "dashboard"  # Navigate back to dashboard
        st.rerun()
    st.header("Stock seniment page")
    st.write("Enter a sentence to predict its sentiment and confidence level.")
    input_stock = st.text_input("Which stock would you like to see?")
    if st.button("Submit"):
        make_table()
        #articles = get_news(input_stock)
        sentiment = stock_sentiment(input_stock)
        #st.text_area(f'"Prediction results: " {sentiment}')
        col1, col2, col3 = st.columns(3)
        col1.write(f"Negative: {sentiment['negative'] * 100:.2f}%")
        col2.write(f"Neutral: {sentiment['neutral'] * 100:.2f}%")
        col3.write(f"Positive: {sentiment['positive'] * 100:.2f}%")
        insert_sentiment(st.session_state.user, input_stock, sentiment['biggest'], sentiment['negative'], sentiment['neutral'], sentiment['positive'])
        st.write("Sentiment results have been saved to the database")
        graph = make_graph(input_stock)
        if isinstance(graph, str):
            st.write(graph)
        else:
            st.line_chart(graph.set_index('Time'))
    
def stock_sentiment(stock, news=None):
    # This function will be used to get the sentiment of a stock
    if not news: news = get_news(stock=stock)
    results = []
    for header in news:
        text_vector = vectorizer.transform([header])
        prediction = model.predict(text_vector)[0]
        probabilities = model.predict_proba(text_vector)[0]
        
        class_probabilities = {label: prob for label, prob in zip(model.classes_, probabilities)}
        results.append(class_probabilities)
    #print(len(results))
                
    overall = overall_sentiment(results)
    overall['biggest'] = max(overall)
    #print(overall)
    return overall
    

def overall_sentiment(results):
    # This function will be used to get the overall sentiment of a stock given results of all articles
    avg_prob = {'negative': 0, 'neutral': 0, 'positive': 0}
    for result in results:
        for label, prob in result.items():
            avg_prob[label] += prob
    for key in avg_prob:
        avg_prob[key] /= len(results) #find percentages of each sentiment
    return avg_prob
    
        

def get_news(stock):
    # This function will be used to get the news of a stock
    data = yf.Ticker(stock)
    news = data.news
    headlines = []
    for story in news:
        headlines.append(story['title'])
    return headlines



def analyze_and_store_sentiment(stock, class_probabilities):
    """Simulate the sentiment analysis and store it in the database."""
    sentiment = max(class_probabilities, key=class_probabilities.get)
    insert_sentiment(st.session_state.user, stock, sentiment, 
                     class_probabilities['negative'], 
                     class_probabilities['neutral'], 
                     class_probabilities['positive'])
    st.write(f"Analysis stored: {stock} - {sentiment}")
    
def make_graph(stock):
    # This function will be used to make a graph of the sentiment of a stock given results previously found
    records = get_stock_records(stock)
    if records is None:
        return "There are no records for this stock"
    times = []
    sentiments = []
    for record in records:
        # for every record, we will see which emotion (neg, neut, pos) is the greatest and store that
        if record[2] > record[3] and record[2] > record[4]:
            sentiments.append(-1 * record[2])
        elif record[3] > record[2] and record[3] > record[4]:
            sentiments.append(record[3])
        else:
            sentiments.append(1+record[4])
        times.append(record[-1])
    #print(sentiments)
    #print(times)
    df = pd.DataFrame({
        'Time': times,
        'Sentiment': sentiments
    })
    return df
    
        


    
        

if __name__ == '__main__':
    #print(get_news("AAPL"))
    print(stock_sentiment("AAPL", get_news("AAPL")))
    print(make_graph("AAPL"))