import streamlit as st
import pandas as pd
import pickle
import numpy as np

from sklearn.ensemble import RandomForestRegressor
from pycaret.classification import *

hdp_model = load_model('hdp_model_19-10-2021 23-58-07')

attrib_info = """
#### Attribute Information:
    - Age
    - Sex
    - Chest Pain Type
    - Resting BP
    - Cholesterol
    - Fasting BS
    - Resting ECG
    - Max HR
    - Exercise Angina
    - Oldpeak
    - ST Slope

"""

def get_fvalue(val):
    feature_dict = {'No':0, 'Yes':1}
    for key, value in feature_dict.items():
        if val == key:
            return value

def get_value(val, my_dict):
    for key, value in my_dict.items():
        if val == key:
            return value

def run_ml_app():

    st.subheader('From ML Section')
    
    with st.expander('Attribute Info'):
        st.markdown(attrib_info)
    
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input('Age')
        sex = st.radio('Sex',['M','F'])
        chest_pain_type = st.radio('Chest Pain Type',['ASY','NAP','ATA','TA'])
        resting_bp = st.number_input('Resting BP',step=1)
        cholesterol = st.number_input('Cholesterol',step=1)
        

    with col2:
        fasting_bs = st.number_input('Fasting BS',step=1)
        resting_ecg = st.radio('Resting ECG',['Normal','LVH','ST'])
        max_hr = st.number_input('Max Heart Rate',step=1)
        exercise_angina = st.radio('Exercise Angina',['Yes','No'])
        oldpeak = st.number_input('Oldpeak',step=0.1)
        st_slope = st.radio('ST Slope',['Up','Down','Flat'])
        

    with st.expander('Selected Options'):
        result = {
            'Age':age,
            'Sex':sex,
            'ChestPainType':chest_pain_type,
            'RestingBP':resting_bp,
            'Cholesterol':cholesterol,
            'FastingBS':fasting_bs,
            'RestingECG':resting_ecg,
            'MaxHR':max_hr,
            'ExerciseAngina':exercise_angina,
            'Oldpeak':oldpeak,
            'ST_Slope':st_slope,
        }

        st.write(result)

        encoded_result = []
        for i in result.values():
            encoded_result.append(i)


        df = pd.DataFrame(result, index=[0])

    with st.expander('Prediction Result'):

        single_sample = df
        result = predict_model(hdp_model, data=single_sample)
        prognostic = result['Label'].values[0]
        # score = result['Score'].values[0]

        if prognostic == 1:
            st.warning('Prognostic: Be careful... You may have some heart disease.')
        else:
            st.success('Prognostic: Congrats!!! You may have a healthy heart, keep going!')