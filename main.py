import streamlit as st

# Title
st.title("Fractional Excretion of Urea (FEUrea) Calculator")

# Input fields
urine_urea = st.number_input("Urine Urea (mg/dL)", min_value=0.0, format="%.2f")
plasma_urea = st.number_input("Plasma Urea (mg/dL)", min_value=0.0, format="%.2f")
urine_creatinine = st.number_input("Urine Creatinine (mg/dL)", min_value=0.0, format="%.2f")
plasma_creatinine = st.number_input("Plasma Creatinine (mg/dL)", min_value=0.0, format="%.2f")

# Calculate FEUrea
if st.button("Calculate FEUrea"):
    if plasma_urea == 0 or urine_creatinine == 0:
        st.error("Plasma Urea and Urine Creatinine must be greater than 0.")
    else:
        feu = (urine_urea * plasma_creatinine) / (plasma_urea * urine_creatinine) * 100
        st.success(f"FEUrea: {feu:.2f}%")
