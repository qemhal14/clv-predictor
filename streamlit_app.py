import streamlit as st

st.title("🚗 Auto Insurance Company")
st.info("This is a machine learning app to predict customer lifetime value.")

# Manual input for single prediction
with st.sidebar:
  st.header("Input Features")
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
  VehicleSize = st.selectbox("Vehicle Class",("Small", "Medsize", "Large"))
  
  
