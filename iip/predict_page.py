import streamlit as st
import pickle
import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.preprocessing import LabelEncoder

def load_model():
    with open('xgb_model.pkl', 'rb') as file:
        loaded_model = pickle.load(file)
    return loaded_model

def show_predict_page():
    st.write("""### Please, fill some information to check on your loan approvals""")
    loaded_model = load_model()

    # Apply custom CSS for styling
    st.markdown("""
        <style>
            .stButton button {
                background-color: red;
                color: white;
            }
            .approved {
                color: green;
                font-weight: bold;
            }
            .rejected {
                color: red;
                font-weight: bold;
            }
        </style>
    """, unsafe_allow_html=True)

    # Collecting input data
    no_of_dependents = st.number_input("No of dependents", value=None, placeholder="Type a number...")
    education = st.selectbox("Education Level", options=["Graduate", "Not Graduate"], placeholder="Select Education level...")
    self_employed = st.selectbox("Self-Employed", options=["Yes", "No"], placeholder="select...")
    income_annum = st.number_input("Annual Income", value=None, placeholder="Type a number....")
    loan_amount = st.number_input("Amount of Loan", value=None, placeholder="Enter Loan amount...")
    loan_term = st.number_input("Loan Term", value=None, placeholder="Enter loan terms in year...")
    cibil_score = st.number_input("Cibil Score", value=None, placeholder="Enter your cibil score")
    residential_assets_value = st.number_input("Residential Asset Value", value=None, placeholder="Enter the value of your residential asset..")
    commercial_assets_value = st.number_input("Commercial Assets Value", value=None, placeholder="Enter your commercial asset value...")
    luxury_assets_value = st.number_input("Luxury Assets Value", value=None, placeholder="Enter your luxury asset value...")
    bank_asset_value = st.number_input("Bank Assets Value", value=None, placeholder="Enter your bank asset value...")

    submit = st.button("Check Loan status")
    if submit:
        input_data = pd.DataFrame({
            'no_of_dependents': [no_of_dependents],
            'education': [education],
            'self_employed': [self_employed],
            'income_annum': [income_annum],
            'loan_amount': [loan_amount],
            'loan_term': [loan_term],
            'cibil_score': [cibil_score],
            'residential_assets_value': [residential_assets_value],
            'commercial_assets_value': [commercial_assets_value],
            'luxury_assets_value': [luxury_assets_value],
            'bank_asset_value': [bank_asset_value]
        })

        # Encoding categorical variables
        le = LabelEncoder()
        input_data['education'] = le.fit_transform(input_data['education'])
        input_data['self_employed'] = le.fit_transform(input_data['self_employed'])

        # Prediction using the loaded model
        prediction = loaded_model.predict(input_data)

        # Display the prediction result
        if prediction[0] == 0:
            st.markdown('<p class="approved">Loan Status: Approved</p>', unsafe_allow_html=True)
        else:
            st.markdown('<p class="rejected">Loan Status: Rejected</p>', unsafe_allow_html=True)

        st.write(f"### Client Information")
        st.write(input_data)
