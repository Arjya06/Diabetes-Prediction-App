from flask import Flask, request, jsonify
import pickle
import pandas as pd
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("diabetes_model.pkl")


@app.route("/")
def home():
    return "Diabetes Prediction API Running"

@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()
    print("Received:", data)

    if data is None:
        return jsonify({"error": "No JSON received"}), 400

    # Maintain column order
    sample = pd.DataFrame([data])[model.feature_names_in_]

    prediction = model.predict(sample)

    result = "Diabetic" if prediction[0] == 1 else "Non-Diabetic"

    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)
