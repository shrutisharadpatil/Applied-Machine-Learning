import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import pickle

def train_and_save():
    try:
        train = pd.read_csv('../Assignment2/data/train.csv')

        if 'text' not in train.columns or 'label' not in train.columns:
            raise ValueError("Missing 'text' or 'label' column in train.csv")

        vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
        X_train = vectorizer.fit_transform(train['text']).toarray()
        y_train = train['label']

        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        with open('model.pkl', 'wb') as f:
            pickle.dump(model, f)
        with open('vectorizer.pkl', 'wb') as f:
            pickle.dump(vectorizer, f)

        print("Model & Vectorizer saved successfully!")

    except Exception as e:
        print(f" Error: {e}")

if __name__ == '__main__':
    train_and_save()
