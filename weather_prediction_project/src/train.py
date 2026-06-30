import pandas as pd
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load Dataset
df = pd.read_csv("dataset/weather.csv")

print("First 5 Rows")
print(df.head())

print("\nDataset Information")
print(df.info())

print("\nMissing Values")
print(df.isnull().sum())

# Fill Missing Values
df.fillna(df.mean(numeric_only=True), inplace=True)

# Data Visualization
plt.figure(figsize=(8,5))
plt.plot(df["Temperature"], marker="o")
plt.title("Temperature Trend")
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.grid(True)
plt.show()

# Features and Target
X = df[["Humidity", "WindSpeed", "Pressure"]]
y = df["Temperature"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
prediction = model.predict(X_test)

print("\nActual Values")
print(y_test.values)

print("\nPredicted Values")
print(prediction)

# Evaluation
mae = mean_absolute_error(y_test, prediction)
r2 = r2_score(y_test, prediction)

print("\nMean Absolute Error:", mae)
print("R2 Score:", r2)

# Save Model
joblib.dump(model, "models/weather_model.pkl")

print("\nModel Saved Successfully!")