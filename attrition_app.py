#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
# Input fields
Age = st.slider('Age of the employee', 0, 100)
Gender = st.selectbox('Gender', ['Male', 'Female'])
DistanceFromHome= st.slider('Distance from home', 1, 29)
TotalWorkingYears = st.number_input('Total Working Years', min_value=0, value=5)
YearsInCurrentRole = st.number_input('Years in Current Role', min_value=0, value=18)
Department = st.selectbox('Department', ['Sales', 'Research & Development', 'Human Resources'])
BusinessTravel= st.selectbox('Business Travel', ['Travel_Rarely', 'Travel_Frequently', 'Non-Travel'])
MonthlyIncome = st.number_input('Monthly Income', min_value=1000, value=19999)
StockOptionLevel=st.slider('Stock Option Level', 0, 3)
JobSatisfaction=st.slider('Job Satisfactionr Level', 1, 4)
EnvironmentSatisfaction=st.slider('Environment Satisfaction Level', 1, 4)
WorkLifeBalance=st.slider('Work-Life balnce Level', 1, 4)
OverTime= st.selectbox('Over Time', ['Yes', 'No'])
JobLevel=st.slider('Job Level', 1, 4)
Education=st.slider('Education Level', 1, 5)

# Create a DataFrame
data = {
    'Age': Age,
    'Gender': Gender,
    'TotalWorkingYears': TotalWorkingYears,
    'YearsInCurrentRole': YearsInCurrentRole,
    'Department': Department,
    'BusinessTravel': BusinessTravel,
    'MonthlyIncome': MonthlyIncome,
    'StockOptionLevel': StockOptionLevel,
    'JobSatisfaction':JobSatisfaction,
    'EnvironmentSatisfaction':EnvironmentSatisfaction,
    'WorkLifeBalance':WorkLifeBalance,
    'OverTime':OverTime,
    'DistanceFromHome':DistanceFromHome,
    'JobLevel':JobLevel,
    'Education':Education
}

df = pd.DataFrame(data, index=[0])

# Dummification
# columns_to_dummify = ['Embarked', 'Title', 'GenderClass']

if df['Department'][0] == 'Sales':
    df['Department_Sales'] = 1
    df['Department_Research & Development'] = 0
    df['Department_Human Resources'] = 0
elif df['Department'][0] == 'Research & Development':
    df['Department_Sales'] = 0
    df['Department_Research & Development'] = 1
    df['Department_Human Resources'] = 0
else:
    df['Department_Sales'] = 0
    df['Department_Research & Development'] = 0
    df['Department_Human Resources'] = 1
    
if df['BusinessTravel'][0] == 'Travel_Rarely':
    df['BusinessTravel_Travel_Rarely'] = 1
    df['BusinessTravel_Travel_Frequently'] = 0
    df['BusinessTravel_Non-Travel'] = 0
elif df['BusinessTravel'][0] == 'Travel_Frequently':
    df['BusinessTravel_Travel_Rarely'] = 0
    df['BusinessTravel_Travel_Frequently'] = 1
    df['BusinessTravel_Non-Travel'] = 0
else:
    df['BusinessTravel_Travel_Rarely'] = 0
    df['BusinessTravel_Travel_Frequently'] = 0
    df['BusinessTravel_Non-Travel'] = 0
    
if df['Gender'][0] == 'Male':
    df['Gender_Male'] = 1
    df['Gender_Female'] = 0
else:
    df['Gender_Male'] = 0
    df['Gender_Female'] = 1
    
if df['OverTime'][0] == 'Yes':
    df['OverTime_Yes'] = 1
    df['OverTime_No'] = 0
else:
    df['OverTime_Yes'] = 0
    df['OverTime_No'] = 1
    
df.drop(['Department', 'BusinessTravel', "Gender","OverTime"], axis=1, inplace=True)


df = df[['Age', 'Gender_Male', 'TotalWorkingYears', 'YearsInCurrentRole', 'Department_Sales', 
       'Department_Research & Development', 'BusinessTravel_Travel_Rarely', 'BusinessTravel_Travel_Frequently', 'MonthlyIncome',
       'StockOptionLevel', 'JobSatisfaction','EnvironmentSatisfaction','WorkLifeBalance','OverTime_No','DistanceFromHome',
         'JobLevel','Education']]

# Prediction
prediction = model.predict(df)
if prediction[0] == 0:
    st.error("The employee stays at the company.")
else:
    st.success("The employee leaves the company.")
st.write(prediction[0])

