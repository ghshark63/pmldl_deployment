import streamlit as st
import requests
import os

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

def check_health():
    response = requests.get(f"{BACKEND_URL}/health")
    return response.json()

def predict(data):
    response = requests.post(f"{BACKEND_URL}/predict", json=data)
    return response.json()

st.title("Diabete status prediction")

with st.expander("Health Check", expanded=False):
    if st.button("Check Health"):
        health_status = check_health()
        st.write("Health Status:", health_status)

with st.expander("Prediction", expanded=True):
    with st.form("predict_form"):
        st.subheader("Input metrics")

        col1, col2 = st.columns(2)

        with col1:
            age = st.slider("Age", -0.1, 0.2, 0.0, 0.01)
            sex = st.selectbox("Sex", options=[-0.1, 0.1], format_func=lambda x: "Male" if x > 0 else "Female")
            bmi = st.slider("BMI - body mass index ", -0.1, 0.2, 0.0, 0.01)
            bp = st.slider("Blood pressure", -0.2, 0.2, 0.0, 0.01)
            s1 = st.slider("S1 - total serum cholesterol", -0.2, 0.2, 0.0, 0.01)

        with col2:
            s2 = st.slider("S2 - low-density lipoproteins", -0.2, 0.2, 0.0, 0.01)
            s3 = st.slider("S3 - high-density lipoproteins", -0.2, 0.2, 0.0, 0.01)
            s4 = st.slider("S4 - total cholesterol", -0.2, 0.2, 0.0, 0.01)
            s5 = st.slider("S5 - log of serum triglycerides level", -0.2, 0.2, 0.0, 0.01)
            s6 = st.slider("S6 - blood sugar level", -0.2, 0.2, 0.0, 0.01)

        submitted = st.form_submit_button("Submit")

        if submitted:
            data = {
                "age": age,
                "sex": sex,
                "bmi": bmi,
                "bp": bp,
                "s1": s1,
                "s2": s2,
                "s3": s3,
                "s4": s4,
                "s5": s5,
                "s6": s6
            }

            prediction = predict(data)

            result = prediction["prediction"]
            st.write(f"Prediction: {result}")