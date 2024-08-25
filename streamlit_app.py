import streamlit as st

st.title("🚗 Auto Insurance Company")
st.info("This is a machine learning app to predict customer lifetime value.")

# Manual input for single prediction
with st.sidebar:
  st.header("Input Features"):
  State = st.selectbox("State",("Arizona", 'California", 'Nevada", "Oregon", 'Washington"))
  Response = st.selectbox("Response",("Yes", "No"))
  Coverage = st.selectbox("Coverage",("Basic", "Premium", "Extended"))
  Education = st.selectbox("Education",('High School or Below", "College", 'Bachelor", "Master", "Doctor"))
  Employment = st.selectbox("EmploymentStatus",("Employed", "Unemployed", "Medical Leave", Disabled", "Retired"))
  Gender = st.selectbox("Gender",("Male", "Female"))
  Income = st.slider("Income", 0, 99981.00, 34080.00)
