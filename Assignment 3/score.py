import pickle

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

def score(text: str, model, threshold: float):
    X_text = vectorizer.transform([text])  # Transform text using vectorizer
    proba = model.predict_proba(X_text)[0][1]
    prediction = 1 if proba >= threshold else 0
    return prediction, proba

