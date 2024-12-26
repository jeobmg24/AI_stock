from nltk import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import joblib

def tokenize_and_vectorize(text=None):
    # Tokenize the text into words and then vectorize it using TF-IDF
    data = pd.read_csv("data.csv")
    #print(data.head())
    print(data.columns)
    vectorizer = TfidfVectorizer(max_features=5000)
    X = vectorizer.fit_transform(data['Sentence'])
    print(X.shape)
    
    label = data["Sentiment"]
    X_train, X_test, y_train, y_test = train_test_split(X, label, test_size=0.2, random_state=42)
    model = LogisticRegression(class_weight='balanced')
    model.fit(X_train, y_train)
    
    # Save the trained model and vectorizer
    joblib.dump(model, 'sentiment_model.pkl')
    joblib.dump(vectorizer, 'tfidf_vectorizer.pkl')

    # Make predictions
    predictions = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, predictions))
    print(classification_report(y_test, predictions))
    
def calculate_stock():
    pass
    
    
tokenize_and_vectorize()
    