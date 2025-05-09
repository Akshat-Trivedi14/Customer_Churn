import streamlit as st
import pandas as pd
import joblib
import numpy as np
import os

# Set page config
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# Load the model
@st.cache_resource
def load_model():
    try:
        # Try multiple possible model locations
        possible_paths = [
            os.path.join(os.path.dirname(os.path.abspath(__file__)), 'churn_pipeline.pkl'),
            os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models', 'churn_pipeline.pkl'),
            'churn_pipeline.pkl'
        ]
        
        model_path = None
        for path in possible_paths:
            if os.path.exists(path):
                model_path = path
                break
                
        if model_path is None:
            st.error("Model file not found. Please ensure 'churn_pipeline.pkl' exists in the project directory or models folder.")
            return None
            
        return joblib.load(model_path)
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        st.error("Please ensure all dependencies are installed and the model file is valid.")
        return None

# Title and description
st.title("Customer Churn Prediction")
st.write("""
This app predicts whether a customer will churn or not based on their characteristics.
Fill in the customer details below to make a prediction.
""")

# Create two columns for input fields
col1, col2 = st.columns(2)

with col1:
    # Customer Demographics
    st.subheader("Customer Demographics")
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior_citizen = st.selectbox("Senior Citizen", ["Yes", "No"])
    partner = st.selectbox("Partner", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["Yes", "No"])
    
    # Service Information
    st.subheader("Service Information")
    phone_service = st.selectbox("Phone Service", ["Yes", "No"])
    multiple_lines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    
    # Online Services
    st.subheader("Online Services")
    online_security = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
    online_backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
    device_protection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
    tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])

with col2:
    # Streaming Services
    st.subheader("Streaming Services")
    streaming_tv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
    streaming_movies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
    
    # Contract and Billing
    st.subheader("Contract and Billing")
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"])
    payment_method = st.selectbox("Payment Method", [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ])
    
    # Charges and Tenure
    st.subheader("Charges and Tenure")
    tenure_months = st.number_input("Tenure (Months)", min_value=0, max_value=72, value=1)
    monthly_charges = st.number_input("Monthly Charges ($)", min_value=0.0, max_value=200.0, value=50.0)
    total_charges = st.number_input("Total Charges ($)", min_value=0.0, max_value=10000.0, value=1000.0)
    cltv = st.number_input("Customer Lifetime Value", min_value=0, max_value=10000, value=3000)
    churn_score = st.number_input("Churn Score", min_value=0, max_value=100, value=50)

# Create a button for prediction
if st.button("Predict Churn"):
    # Create a dictionary with all the input values
    input_data = {
        'Gender': gender,
        'Senior Citizen': senior_citizen,
        'Partner': partner,
        'Dependents': dependents,
        'Phone Service': phone_service,
        'Multiple Lines': multiple_lines,
        'Internet Service': internet_service,
        'Online Security': online_security,
        'Online Backup': online_backup,
        'Device Protection': device_protection,
        'Tech Support': tech_support,
        'Streaming TV': streaming_tv,
        'Streaming Movies': streaming_movies,
        'Contract': contract,
        'Paperless Billing': paperless_billing,
        'Payment Method': payment_method,
        'Tenure Months': tenure_months,
        'Monthly Charges': monthly_charges,
        'Total Charges': total_charges,
        'CLTV': cltv,
        'Churn Score': churn_score,
        'Country': 'United States',  # Default value
        'State': 'California',       # Default value
        'City': 'Los Angeles',       # Default value
        'Churn Label': 'No'          # Default value
    }
    
    # Convert to DataFrame
    input_df = pd.DataFrame([input_data])
    
    # Load model and make prediction
    model = load_model()
    prediction = model.predict(input_df)
    probability = model.predict_proba(input_df)
    
    # Display results
    st.subheader("Prediction Results")
    if prediction[0] == 1:
        st.error("This customer is likely to churn!")
    else:
        st.success("This customer is likely to stay!")
    
    # Display probability
    st.write(f"Probability of churn: {probability[0][1]:.2%}")
    
    # Display some insights
    st.subheader("Insights")
    if prediction[0] == 1:
        st.write("""
        **Recommendations to prevent churn:**
        - Consider offering a loyalty discount
        - Review the customer's service package
        - Reach out to understand their concerns
        - Consider upgrading their service
        """)
    else:
        st.write("""
        **Customer retention is strong!**
        - Continue providing excellent service
        - Consider upselling opportunities
        - Maintain regular communication
        """)

# Add footer
st.markdown("---")
st.markdown("Built with using Streamlit") 