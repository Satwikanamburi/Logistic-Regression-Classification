#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import numpy as np
import joblib

# Load the trained model and scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("Diabetes Prediction using Logistic Regression")

st.write("Enter the patient's details below.")

# User Inputs
pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=1)
glucose = st.number_input("Glucose", min_value=0.0, value=120.0)
blood_pressure = st.number_input("Blood Pressure", min_value=0.0, value=70.0)
skin_thickness = st.number_input("Skin Thickness", min_value=0.0, value=20.0)
insulin = st.number_input("Insulin", min_value=0.0, value=80.0)
bmi = st.number_input("BMI", min_value=0.0, value=30.0)
diabetes_pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.0, value=0.5)
age = st.number_input("Age", min_value=1, max_value=120, value=30)

# Prediction Button
if st.button("Predict"):

    data = np.array([[pregnancies,
                      glucose,
                      blood_pressure,
                      skin_thickness,
                      insulin,
                      bmi,
                      diabetes_pedigree,
                      age]])

    data = scaler.transform(data)

    prediction = model.predict(data)
    probability = model.predict_proba(data)

    if prediction[0] == 1:
        st.error("The patient is likely to have Diabetes.")
    else:
        st.success("The patient is not likely to have Diabetes.")

    st.write("Prediction Probability:")
    st.write(probability)

