import streamlit as st
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder

st.title("🚗 Auto Insurance Company")
st.info("This is a machine learning app to predict customer lifetime value.")

# Manual input for single prediction
with st.sidebar:
  st.header("Input Data")
  State = st.selectbox("State",("Arizona", "California", "Nevada", "Oregon", "Washington"))
  Response = st.selectbox("Response",("Yes", "No"))
  Coverage = st.selectbox("Coverage",("Basic", "Premium", "Extended"))
  Education = st.selectbox("Education",("High School or Below", "College", "Bachelor", "Master", "Doctor"))
  EmploymentStatus = st.selectbox("Employment",("Employed", "Unemployed", "Medical Leave", "Disabled", "Retired"))
  Gender = st.selectbox("Gender",("Male", "Female"))
  Income = st.slider("Income", 10037.00, 99981.00, 34080.00)
  LocationCode = st.selectbox("Location",("Suburban", "Rural", "Urban"))
  MaritalStatus = st.selectbox("Matiral Status",("Single", "Married", "Divorced"))
  MonthlyPremiumAuto = st.slider("Monthly Premium", 61.0, 298.0, 83.0)
  MonthsSinceLastClaim = st.slider("Months Since Last Claim", 0, 35, 14)
  MonthsSincePolicyInception = st.slider("Months Since Policy Inception", 0, 99, 48)
  NumberofOpenComplaints = st.slider("Number of Open Complaints", 0, 5, 1)
  NumberofPolicies = st.slider("Number of Policies", 1, 9, 2)
  PolicyType = st.selectbox("Policy Type",("Personal Auto", "Special Auto", "Corporate Auto"))
  Policy = st.selectbox("Policy",("Personal L1", "Personal L2", "Personal L3", "Special L1", "Special L2", "Special L3", "Corporate L1", "Corporate L2", "Corporate L3"))
  RenewOfferType = st.selectbox("Renew Offer",("Offer1", "Offer2", "Offer3", "Offer4"))
  SalesChannel = st.selectbox("Sales Channel",("Agent", "Branch", "Web", "Call Center"))
  TotalClaimAmount = st.slider("Total Claim Amount", 0.00, 2893.23, 384.00)
  VehicleClass = st.selectbox("Vehicle Class",("Four-Door Car", "Two-Door Car", "SUV", "Sports Car", "Luxury SUV", "Luxury Car"))
  VehicleSize = st.selectbox("Vehicle Size",("Small", "Medsize", "Large"))

# Create Dataframe for Input Features
data = {
  "State":State,
  "Response":Response,
  "Coverage":Coverage,
  "Education":Education,
  "EmploymentStatus":EmploymentStatus,
  "Gender":Gender,
  "Income":Income,
  "Location Code":LocationCode,
  "Marital Status":MaritalStatus,
  "Monthly Premium Auto":MonthlyPremiumAuto,
  "Months Since Last Claim":MonthsSinceLastClaim,
  "Months Since Policy Inception":MonthsSincePolicyInception,
  "Number of Open Complaints":NumberofOpenComplaints,
  "Number of Policies":NumberofPolicies,
  "Policy Type":PolicyType,
  "Policy":Policy,
  "Renew Offer Type":RenewOfferType,
  "Sales Channel":SalesChannel,
  "Total Claim Amount":TotalClaimAmount,
  "Vehicle Class":VehicleClass,
  "Vehicle Size":VehicleSize
}

st.write("Inputed Single Data for Prediction.")
input_df = pd.DataFrame(data, index=[0])
input_df

# Encoding
onehot_columns = ['State', 'Response', 'Coverage', 'EmploymentStatus', 'Gender', 'Location Code', 'Marital Status', 'Policy Type', 'Policy', 'Renew Offer Type', 'Sales Channel', 'Vehicle Size']
ordinal_columns = ['Education', 'Vehicle Class']

# Define the categories for ordinal encoding
education_categories = ['High School or Below', 'College', 'Bachelor', 'Master', 'Doctor']
vehicle_class_categories = ['Four-Door Car', 'Two-Door Car', 'SUV', 'Sports Car', 'Luxury SUV', 'Luxury Car']

# Ordinal encoding
ordinal_encoder = OrdinalEncoder(categories=[education_categories, vehicle_class_categories])
encoded_ordinal = ordinal_encoder.fit_transform(input_df[ordinal_columns])
encoded_ordinal_df = pd.DataFrame(encoded_ordinal)

# One-hot encoding
onehot_encoder = OneHotEncoder(sparse_output=False, drop='first')
encoded_onehot = onehot_encoder.fit_transform(input_df[onehot_columns])
encoded_onehot_df = pd.DataFrame(encoded_onehot, columns=onehot_encoder.get_feature_names_out(onehot_columns))

# Remaining column
remaining_df = input_df[['Income', 'Monthly Premium Auto', 'Months Since Last Claim', 'Months Since Policy Inception', 'Number of Open Complaints', 'Number of Policies', 'Total Claim Amount']]

# Combine original non-encoded columns with the encoded one-hot columns
final_df = pd.concat([encoded_ordinal_df.reset_index(drop=True), encoded_onehot_df.reset_index(drop=True), remaining_df.reset_index(drop=True)], axis=1)

st.write("Encoded Data for Prediction:")
st.write(final_df)

  
