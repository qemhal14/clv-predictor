import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
from sklearn.compose import ColumnTransformer
import pickle

st.title("🚗 Auto Insurance Company")
st.info("This is a machine learning app to predict customer lifetime value.")

st.title("Dashboard")
html_code = """
<div class='tableauPlaceholder' id='viz1728219711852' style='position: relative'>
    <noscript><a href='#'>
        <img alt='Customer Overview' src='https://public.tableau.com/static/images/Fi/FinproDashboard_17237922279380/CustomerOverview/1_rss.png' style='border: none' />
    </a></noscript>
    <object class='tableauViz' style='display:none;'>
        <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
        <param name='embed_code_version' value='3' /> 
        <param name='path' value='views/FinproDashboard_17237922279380/CustomerOverview?:language=en-US&:embed=true&:sid=&:redirect=auth' /> 
        <param name='toolbar' value='yes' />
        <param name='static_image' value='https://public.tableau.com/static/images/Fi/FinproDashboard_17237922279380/CustomerOverview/1.png' /> 
        <param name='animate_transition' value='yes' />
        <param name='display_static_image' value='yes' />
        <param name='display_spinner' value='yes' />
        <param name='display_overlay' value='yes' />
        <param name='display_count' value='yes' />
        <param name='language' value='en-US' />
    </object>
</div>
<script type='text/javascript'>
    var divElement = document.getElementById('viz1728219711852');
    var vizElement = divElement.getElementsByTagName('object')[0];
    if (divElement.offsetWidth > 800) { 
        vizElement.style.width='1366px'; 
        vizElement.style.height='795px'; 
    } else if (divElement.offsetWidth > 500) { 
        vizElement.style.width='1366px'; 
        vizElement.style.height='795px'; 
    } else { 
        vizElement.style.width='100%'; 
        vizElement.style.height='2877px'; 
    } 
    var scriptElement = document.createElement('script');
    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
    vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>
"""

# Use Streamlit's components.html() to embed the Tableau dashboard
st.components.v1.html(html_code, height=800)

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


