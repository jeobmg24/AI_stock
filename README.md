# AI sentiment for stocks
Machine learning project to track the sentiment of stocks

## 1. Project Description
This is a personal project that is made to track the sentiment of stocks. Once logged in, 
You can head over to the "Stock Sentiment" tab, where you can input any Ticker, and using
the Headlines found about that stock on Yahoo Finance, it will return the positive, negative, 
and neutral sentiment surrounding the stock. It will then save that data to a database and 
show a graph in which it will show your result in relation to other times the stock has been 
searched.

## 2. Features
When you open the app, you will be navigated to the login page. Here, you can either sign in with an existing account
or have the option to make an account. When you make an account, it will remember you account info to sign in with and also for
certain features in the app. 

Once logged in, you can navigate to the 'stock sentiment' tab and enter the ticker of any stock. Using the Yahoo Finance API, it will get recent headlines about that 
stock and analyze them using the AI model that I trained using headlines and their sentiment. It will return percentages based on how positive, neutral, and negative
it believes those headlines to be. A chart will appear below the results showing how the sentiment of the stock changed over time. This chart will use saved results where other users have
searched up this stock. Finally, your search results will be saved to the database

On the 'check database' tab, you can check all the results of searches you have queried. It will show the stock searched, the overall sentiment, and the date searched

## 3. What I learned
From this project, I both learned and also reinforced many of my skills. Some of the new skills I learned are:
* How to build an AI model, train it, and feed it with new data
* Using streamlit, navigating its controls and widgets
* Using sqllite3 for Python

Some skills that I reinforced were:

* Using great coding practices in Python
* Using SQL and queries to the database
* Using APIs to get data from a third party application
* Using documentation to figure out new libraries


### What I hope to add
Though I felt this project was good enough to post on GitHub, I do not consider this project 
anywhere close to a finished product. I hope to include some of these features in the near future:

* Database for accounts so that you can sign up and your login will be remembered
* More engaging app with colors and more interactive widgets
* Train the model with more data and continue to update it
