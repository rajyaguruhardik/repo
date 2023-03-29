# ai_models/doji_recognition.py

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pickle

def create_features_and_labels(df):
    # Add your feature extraction code here
    # Calculate additional features
    df['price_range'] = df['High'] - df['Low']
    df['body_size'] = abs(df['Open'] - df['Close'])
    df['upper_shadow'] = df['High'] - df[['Open', 'Close']].max(axis=1)
    df['lower_shadow'] = df[['Open', 'Close']].min(axis=1) - df['Low']

    # Define the Doji pattern
    df['doji'] = (df['body_size'] / df['price_range']) <= 0.1

    # Select the features and the target variable
    features = df[['Open', 'High', 'Low', 'Close', 'price_range', 'body_size', 'upper_shadow', 'lower_shadow']].values
    labels = df['doji'].values

    # Select the features and the target variable
    features = df[['Open', 'High', 'Low', 'Close']].values
    labels = df['doji'].values

    return features, labels

def train_and_save_model(df):
    features, labels = create_features_and_labels(df)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

    # Train the Support Vector Machine model
    model = SVC()
    model.fit(X_train, y_train)

    # Check the model's accuracy
    y_pred = model.predict(X_test)
    print("Model accuracy:", accuracy_score(y_test, y_pred))

    # Save the trained model
    with open('ai_models/trained_models/doji_svm_model.pkl', 'wb') as f:
        pickle.dump(model, f)

# Load your data in a pandas DataFrame
# Example:
# df = pd.read_csv('your_data.csv')

# Uncomment and run the following line after setting up your DataFrame:
# train_and_save_model(df)
