from flask import Flask, request, jsonify
import joblib
from score import score
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)  # Allows access via ngrok

# Load the trained model
model = joblib.load('model.pkl')

@app.route('/score', methods=['POST'])
def score_endpoint():
    data = request.get_json()
    text = data.get('text', '')
    threshold = data.get('threshold', 0.5)

    prediction, propensity = score(text, model, threshold)

    return jsonify({'prediction': prediction, 'propensity': propensity})

if __name__ == '__main__':
    app.run
