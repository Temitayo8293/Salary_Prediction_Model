
import streamlit as st
import pandas as pd
import joblib

# Load your saved model
model = joblib.load("salary_trained_model_Xgboost.pkl")

st.title("Salary Prediction App")

st.write("Enter employee details:")

# Inputs
experience = st.slider("Years of Experience", 0, 50, 5)
education = st.selectbox("Education Level", ["High School", "Bachelor", "Master", "PhD"])
department = st.selectbox("Department", ["Engineering", "Finance", "HR", "Marketing", "Sales", "Operations"])
years_company = st.slider("Years at Company", 0, 25, 3)
performance = st.slider("Performance Rating", 1, 5, 3)
hours = st.slider("Monthly Hours Worked", 100, 250, 160)

# Create dataframe
input_data = pd.DataFrame({

    'YearsExperience': [experience],
    'YearsAtCompany': [years_company],
    'Department': [department],
    'EducationLevel': [education],
    'PerformanceRating': [performance],
    'MonthlyHoursWorked': [hours]
})

# Predict
if st.button("Predict Salary"):
    prediction = model.predict(input_data)
    st.success(f"Estimated Salary: £{prediction[0]:,.2f}")