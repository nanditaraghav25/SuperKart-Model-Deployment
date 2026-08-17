
# Import necessary libraries
import numpy as np
import joblib
import pandas as pd
from flask import Flask, request, jsonify

# Initialize Flask app
superkart_api = Flask("SuperKart_Sales_API")

# Load the trained sales prediction model
model = joblib.load("superkart_rf_tuned.joblib")

# Define a route for the home page
@superkart_api.get('/')
def home():
    return "Welcome to the SuperKart Sales Prediction API"

# Define an endpoint to predict sales
@superkart_api.post('/v1/predict')
def predict_sales():

    # Get JSON data from the request
    data = request.get_json()

    # Extract features in the same format used during model training
    sample = {
        'Product_Weight': data['Product_Weight'],
        'Product_Sugar_Content': data['Product_Sugar_Content'],
        'Product_Allocated_Area': data['Product_Allocated_Area'],
        'Product_Type': data['Product_Type'],
        'Product_MRP': data['Product_MRP'],
        'Store_Id': data['Store_Id'],
        'Store_Size': data['Store_Size'],
        'Store_Location_City_Type': data['Store_Location_City_Type'],
        'Store_Type': data['Store_Type'],
        'Product_Id_Prefix': data['Product_Id_Prefix'],
        'Store_Age': data['Store_Age']
    }

    # Convert input into DataFrame
    input_data = pd.DataFrame([sample])

    # Make sales prediction
    prediction = model.predict(input_data).tolist()[0]

    # Return prediction as JSON
    return jsonify({'Sales': prediction})


# Run Flask application
if __name__ == '__main__':
    superkart_api.run(debug=True)
