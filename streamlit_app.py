import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
from sklearn.compose import ColumnTransformer
import pickle

st.title("🚗 Auto Insurance Company")
st.info("This is a machine learning app to predict customer lifetime value.")

st.title("Dashboard")
components.iframe(
    "https://public.tableau.com/views/FinproDashboard_17237922279380/CustomerOverview?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link",
    width=1366, height=768
)

# Manual input for single prediction
with st.sidebar:
    st.header("Input Data")
    State = st.selectbox("State", ("Arizona", "California", "Nevada", "Oregon", "Washington"))
    Response = st.selectbox("Response", ("Yes", "No"))
    Coverage = st.selectbox("Coverage", ("Basic", "Premium", "Extended"))
    Education = st.selectbox("Education", ("High School or Below", "College", "Bachelor", "Master", "Doctor"))
    EmploymentStatus = st.selectbox("Employment", ("Employed", "Unemployed", "Medical Leave", "Disabled", "Retired"))
    Gender = st.selectbox("Gender", ("M", "F"))
    Income = st.slider("Income", 10037, 99981, 34080)
    LocationCode = st.selectbox("Location", ("Suburban", "Rural", "Urban"))
    MaritalStatus = st.selectbox("Marital Status", ("Single", "Married", "Divorced"))
    MonthlyPremiumAuto = st.slider("Monthly Premium", 61, 298, 83)
    MonthsSinceLastClaim = st.slider("Months Since Last Claim", 0, 35, 14)
    MonthsSincePolicyInception = st.slider("Months Since Policy Inception", 0, 99, 48)
    NumberofOpenComplaints = st.slider("Number of Open Complaints", 0, 5, 1)
    NumberofPolicies = st.slider("Number of Policies", 1, 9, 2)
    PolicyType = st.selectbox("Policy Type", ("Personal Auto", "Special Auto", "Corporate Auto"))
    Policy = st.selectbox("Policy", ("Personal L1", "Personal L2", "Personal L3", "Special L1", "Special L2", "Special L3", "Corporate L1", "Corporate L2", "Corporate L3"))
    RenewOfferType = st.selectbox("Renew Offer", ("Offer1", "Offer2", "Offer3", "Offer4"))
    SalesChannel = st.selectbox("Sales Channel", ("Agent", "Branch", "Web", "Call Center"))
    TotalClaimAmount = st.slider("Total Claim Amount", 0.00, 2893.23, 384.00)
    VehicleClass = st.selectbox("Vehicle Class", ("Four-Door Car", "Two-Door Car", "SUV", "Sports Car", "Luxury SUV", "Luxury Car"))
    VehicleSize = st.selectbox("Vehicle Size", ("Small", "Medsize", "Large"))

# Create DataFrame for Input Features
data = {
    "State": State,
    "Response": Response,
    "Coverage": Coverage,
    "Education": Education,
    "EmploymentStatus": EmploymentStatus,
    "Gender": Gender,
    "Income": Income,
    "Location Code": LocationCode,
    "Marital Status": MaritalStatus,
    "Monthly Premium Auto": MonthlyPremiumAuto,
    "Months Since Last Claim": MonthsSinceLastClaim,
    "Months Since Policy Inception": MonthsSincePolicyInception,
    "Number of Open Complaints": NumberofOpenComplaints,
    "Number of Policies": NumberofPolicies,
    "Policy Type": PolicyType,
    "Policy": Policy,
    "Renew Offer Type": RenewOfferType,
    "Sales Channel": SalesChannel,
    "Total Claim Amount": TotalClaimAmount,
    "Vehicle Class": VehicleClass,
    "Vehicle Size": VehicleSize
}

st.write("Inputted Single Data for Prediction.")
input_df = pd.DataFrame(data, index=[0])
st.write(input_df)

# Load the trained model
model = pickle.load(open("CLV Predictor.pkl", "rb"))

# Predict the CLV
try:
    prediction = model.predict(input_df)
    st.subheader("Predicted Customer Lifetime Value")
    st.write(f"Predicted CLV: ${prediction[0]:,.2f}")
except ValueError as e:
    st.error(f"Error during prediction: {e}")


