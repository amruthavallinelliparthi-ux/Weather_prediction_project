Weather Prediction System 

Project Description
This project is a Machine Learning-based Weather Prediction System developed using Python and Flask. The application predicts the temperature based on weather parameters such as Humidity, Wind Speed, and Pressure.

Features
- Predicts temperature using Machine Learning.
- User-friendly web interface using Flask.
- Displays predicted temperature instantly.
- Uses Linear Regression algorithm.
- Easy to understand and modify.

Technologies Used
- Python
- Flask
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- HTML
- CSS

Project Structure
Weather_Prediction_Project/
│
├── dataset/
│ └── weather.csv
├── models/
│ └── weather_model.pkl
├── src/
│ └── train.py
├── templates/
│ └── index.html
├── static/
│ └── style.css
├── app.py
├── requirements.txt
├── README.md
└── .gitignore

Installation
1. Clone the repository:
git clone <repository-link>
2. Install dependencies:
pip install -r requirements.txt
3. Train the model:
python src/train.py
4. Run the Flask application:
python app.py
5. Open the browser and visit:
http://127.0.0.1:5000
Input Parameters
- Humidity
- Wind Speed
- Pressure

Output
Predicted Temperature in Celsius (°C).
Future Enhancements
- Add larger weather datasets.
- Improve prediction accuracy using advanced algorithms.
- Add charts and dashboards.
- Store prediction history in a database.
- Deploy the application online.

Author
Nelliparthi Amrutha Valli

License
This project is created for learning and educational purposes.