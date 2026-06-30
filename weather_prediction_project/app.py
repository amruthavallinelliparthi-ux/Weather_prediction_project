from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("models/weather_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    humidity = float(request.form["humidity"])
    windspeed = float(request.form["windspeed"])
    pressure = float(request.form["pressure"])

    data = np.array([[humidity, windspeed, pressure]])
    prediction = model.predict(data)[0]

    return render_template(
        "index.html",
        prediction=round(prediction, 2)
    )

if __name__ == "__main__":
    app.run(debug=True)