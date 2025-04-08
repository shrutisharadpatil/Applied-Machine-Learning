import joblib

# Load vectorizer only
vectorizer = joblib.load("vectorizer.pkl")

def score(text: str, model, threshold: float):
    text_vector = vectorizer.transform([text])
    propensity = model.predict_proba(text_vector)[0][1]
    prediction = int(propensity >= threshold)
    return prediction, propensity
