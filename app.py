from flask import Flask, request, render_template
import joblib
from utils import extract_features, ai_predict  # Centralized feature extraction logic
app = Flask(__name__)

# Load the saved ML model
ml_model = joblib.load("./model/model.pkl")
print("Machine Learning Model loaded successfully!")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    url = request.form.get("url")
    mode = request.form.get("mode")  # Toggle: "ml", "ai", or "both"
    if not url:
        return render_template("index.html", error="Please enter a URL.")

    result_ml, result_ai = None, None

    # Machine Learning Prediction
    if mode in ("ml", "both"):
        features = [extract_features(url)]
        result_ml = "Phishing" if ml_model.predict(features)[0] == 1 else "Legitimate"

    # AI Prediction
    if mode in ("ai", "both"):
        result_ai = ai_predict(url)

    return render_template(
        "index.html",
        url=url,
        result_ml=result_ml,
        result_ai=result_ai,  # Rendered HTML from AI response
    )

if __name__ == "__main__":
    app.run(debug=True)
