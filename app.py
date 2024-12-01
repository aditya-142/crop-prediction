from flask import Flask, request, render_template
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load and preprocess the data
df = pd.read_csv('Crop_Recommendation.csv')
X = df[[
    'Nitrogen', 'Phosphorus', 'Potassium', 'Temperature', 'Humidity', 'pH_Value'
]]
y = df['Crop']

# Split the data and train the model
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.2,
                                                    random_state=42)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Initialize Flask app
app = Flask(__name__)


# Home route to render the input form
@app.route('/')
def home():
    return render_template('index.html')


# Recommendation route to process the input and return the result
@app.route('/recommend', methods=['POST'])
def recommend():
    # Get user input from the form
    nitrogen = float(request.form['nitrogen'])
    phosphorus = float(request.form['phosphorus'])
    potassium = float(request.form['potassium'])
    temperature = float(request.form['temperature'])
    humidity = float(request.form['humidity'])
    ph_value = float(request.form['ph_value'])

    # Predict the crop based on input features
    input_data = [[
        nitrogen, phosphorus, potassium, temperature, humidity, ph_value
    ]]
    predicted_crop = model.predict(input_data)[0]

    # Render result page with the prediction
    return render_template('result.html', crop=predicted_crop)


# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)