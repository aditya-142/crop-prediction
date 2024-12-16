## Crop Recommendation System

### Overview
The Crop Recommendation System is a web-based application designed to assist farmers in selecting the most suitable crop to cultivate based on soil and environmental parameters. The system uses a Random Forest Classifier model to predict the ideal crop by analyzing input parameters such as nitrogen, phosphorus, potassium, temperature, humidity, and pH value.

### Features
- **User-friendly Interface**: Input soil and environmental parameters through a simple web form.
- **Accurate Recommendations**: Utilizes a trained Random Forest Classifier for predictions.
- **Real-time Results**: Provides immediate feedback on the recommended crop.

### Technologies Used
- **Backend**: Flask (Python)
- **Machine Learning**: Random Forest Classifier from `scikit-learn`
- **Frontend**: HTML templates for user interaction
- **Data Handling**: `pandas` for preprocessing
- **Dataset**: `Crop_Recommendation.csv`

### How to Run
1. **Install Dependencies**:
   Ensure you have Python 3.9 installed. Install required libraries using:
   ```bash
   pip install flask pandas scikit-learn
   ```
2. **Place Dataset**:
   Ensure `Crop_Recommendation.csv` is in the same directory as the script.

3. **Run the Application**:
   Start the Flask server by executing:
   ```bash
   python app.py
   ```
   The app will run on `http://0.0.0.0:8080`.

4. **Access the Application**:
   Open a web browser and navigate to `http://localhost:8080`. Input the parameters to get a crop recommendation.

### File Structure
- `app.py`: Main application file containing the Flask app and machine learning model.
- `Crop_Recommendation.csv`: Dataset for training the machine learning model.
- `templates/`: Contains `index.html` for the input form and `result.html` for displaying the recommendation.

### Example Input
- Nitrogen: 20  
- Phosphorus: 10  
- Potassium: 15  
- Temperature: 30°C  
- Humidity: 60%  
- pH Value: 6.5  

### Example Output
- **Recommended Crop**: Wheat

