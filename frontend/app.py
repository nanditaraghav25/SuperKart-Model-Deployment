
import streamlit as st
import pandas as pd
import requests

# Base URL of the Flask backend
BACKEND_URL = "http://backend:7860"

# Set the title of the Streamlit app
st.title("SuperKart Sales Prediction")

# Section for online prediction
st.subheader("Online Sales Prediction")

# Collect user inputs
product_weight = st.number_input(
    "Product Weight",
    min_value=0.0,
    value=12.0
)

product_sugar_content = st.selectbox(
    "Product Sugar Content",
    ["Low Sugar", "Regular", "No Sugar"]
)

product_allocated_area = st.number_input(
    "Product Allocated Area",
    min_value=0.0,
    value=0.05,
    format="%.3f"
)

product_type = st.selectbox(
    "Product Type",
    [
        "Baking Goods",
        "Breads",
        "Breakfast",
        "Canned",
        "Dairy",
        "Frozen Foods",
        "Fruits and Vegetables",
        "Hard Drinks",
        "Health and Hygiene",
        "Household",
        "Meat",
        "Others",
        "Seafood",
        "Snack Foods",
        "Soft Drinks",
        "Starchy Foods"
    ]
)

product_mrp = st.number_input(
    "Product MRP",
    min_value=0.0,
    value=150.0
)

store_id = st.selectbox(
    "Store ID",
    ["OUT001", "OUT002", "OUT003", "OUT004"]
)

store_size = st.selectbox(
    "Store Size",
    ["Small", "Medium", "High"]
)

store_location = st.selectbox(
    "Store Location City Type",
    ["Tier 1", "Tier 2", "Tier 3"]
)

store_type = st.selectbox(
    "Store Type",
    [
        "Departmental Store",
        "Supermarket Type 1",
        "Supermarket Type 2",
        "Food Mart"
    ]
)

product_id_prefix = st.text_input(
    "Product ID Prefix",
    value="FD"
)

store_age = st.number_input(
    "Store Age",
    min_value=0,
    value=17
)

# Create input dictionary
input_data = {
    "Product_Weight": product_weight,
    "Product_Sugar_Content": product_sugar_content,
    "Product_Allocated_Area": product_allocated_area,
    "Product_Type": product_type,
    "Product_MRP": product_mrp,
    "Store_Id": store_id,
    "Store_Size": store_size,
    "Store_Location_City_Type": store_location,
    "Store_Type": store_type,
    "Product_Id_Prefix": product_id_prefix,
    "Store_Age": store_age
}

# Make prediction when Predict button is clicked
if st.button("Predict Sales", type="primary"):

    try:
        response = requests.post(
            f"{BACKEND_URL}/v1/predict",
            json=input_data
        )

        if response.status_code == 200:

            prediction = response.json()["Sales"]

            st.success(
                f"Predicted Product Sales: ${prediction:,.2f}"
            )

        else:
            st.error(
                f"Prediction API returned error: {response.status_code}"
            )

    except requests.exceptions.RequestException:
        st.error("Unable to connect to the prediction API.")
