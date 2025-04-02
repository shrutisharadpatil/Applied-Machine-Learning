import pickle
from flask import Flask, request, jsonify
from score import score

app = Flask(__name__)

# Load trained model and vectorizer
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route('/score', methods=['POST'])
def get_score():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    prediction, propensity = score(text, model, threshold=0.7)
    response = {
        "prediction": prediction,
        "propensity": propensity,
        "classification": "SPAM" if prediction else "NOT SPAM"
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
