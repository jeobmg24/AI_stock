import sqlite3
import streamlit as st
import datetime
import os
def make_table():
    print(os.getcwd())
    conn = sqlite3.connect("stock_sentiment.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS stock_sentiments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user TEXT, 
                    stock TEXT,
                    sentiment TEXT,
                    negative REAL,
                    neutral REAL,
                    positive REAL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )''')
    conn.commit()
    conn.close()


def insert_sentiment(user, stock, sentiment, negative, neutral, positive):
    """Insert a sentiment record into the database."""
    conn = sqlite3.connect('stock_sentiment.db')
    c = conn.cursor()
    c.execute('''INSERT INTO stock_sentiments (user, stock, sentiment, negative, neutral, positive) 
                 VALUES (?, ?, ?, ?, ?, ?)''', (user, stock, sentiment, negative, neutral, positive))
    conn.commit()
    conn.close()
    
def get_user_records(user_id):
    conn = sqlite3.connect('stock_sentiment.db')
    c = conn.cursor()
    c.execute('''
        SELECT stock, sentiment, timestamp
        FROM stock_sentiments
        WHERE user = ?
        ORDER BY timestamp DESC
    ''', (user_id,))
    records = c.fetchall()
    conn.close()
    return records

def get_stock_records(stock):
    # this function returns all the previous instances that the given stock has been looked up
    conn = sqlite3.connect('stock_sentiment.db')
    c = conn.cursor()
    #print(c)
    c.execute('''
              SELECT stock, sentiment, negative, neutral, positive, timestamp
              FROM stock_sentiments
              WHERE stock = ?
              ORDER BY timestamp DESC
            ''', (stock,))
    records = c.fetchall()
    conn.close()
    return records



if __name__ == "__main__":
    make_table()

