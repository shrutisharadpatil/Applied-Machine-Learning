import pickle
from flask import Flask, request, jsonify
import numpy as np
from score import score

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb")) # Load the trained model

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    return jsonify({'prediction': prediction.tolist()})


@app.route('/score', methods=['POST'])
def get_score():
    if request.method == 'POST':
        data = request.get_json()
        text = data['text']
        prediction, propensity = score(text, model, threshold=0.7)
        classification = ['NOT SPAM', 'SPAM']
        response = {
            'prediction': prediction,
            'propensity': propensity,
            'Classification': classification[prediction]
        }
        return jsonify(response)

        return """
            <!DOCTYPE html>
            <html lang="en">
            <body>
                <h1>SPAM Classification</h1>
                <form action="/" method="post">
                    <label for="text">Enter Text:</label><br>
                    <input type="text" id="text" name="text"><br><br>
                    <input type="submit" value="Submit">
                </form>
            </body>
            </html>
        """

app.run(debug=True, host='0.0.0.0', port=5000)
