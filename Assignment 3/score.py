import joblib

# Loading the model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")  # Load the vectorizer

def score(text: str, model, threshold: float):
    # Transforming text using vectorizer
    text_vector = vectorizer.transform([text])  # Convert text to numerical features

    # Get the probability
    propensity = model.predict_proba(text_vector)[0][1]  # Assuming binary classification

    # prediction based on threshold
    prediction = int(propensity >= threshold)
    
    return prediction, propensity


