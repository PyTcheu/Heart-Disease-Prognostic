import streamlit as st
from pycaret.classification import *

hdp_model = load_model('hdp_model_19-10-2021 23-58-07')

attrib_info = """
#### Attribute Information:
    Age: age of the patient [years]
    Sex: sex of the patient [M: Male, F: Female]
    ChestPainType: chest pain type [TA: Typical Angina, ATA: Atypical Angina, NAP: Non-Anginal Pain, ASY: Asymptomatic]
    RestingBP: resting blood pressure [mm Hg]
    Cholesterol: serum cholesterol [mm/dl]
    FastingBS: fasting blood sugar [1: if FastingBS > 120 mg/dl, 0: otherwise]
    RestingECG: resting electrocardiogram results [Normal: Normal, ST: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV), LVH: showing probable or definite left ventricular hypertrophy by Estes' criteria]
    MaxHR: maximum heart rate achieved [Numeric value between 60 and 202]
    ExerciseAngina: exercise-induced angina [Y: Yes, N: No]
    Oldpeak: oldpeak = ST [Numeric value measured in depression]
    ST_Slope: the slope of the peak exercise ST segment [Up: upsloping, Flat: flat, Down: downsloping]
    HeartDisease: output class [1: heart disease, 0: Normal]

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
        age = st.number_input('Age',step=1)
        
        resting_bp = st.number_input('Resting BP',step=1)
        cholesterol = st.number_input('Cholesterol',step=1)
        chest_pain_type = st.radio('Chest Pain Type',['ASY','NAP','ATA','TA'])
        oldpeak = st.number_input('Oldpeak',step=0.1)
        max_hr = st.number_input('Max Heart Rate',step=1)

    with col2:
        sex = st.radio('Sex',['M','F'])
        fasting_bs = st.radio('Fasting BS',[1,0])
        resting_ecg = st.radio('Resting ECG',['Normal','LVH','ST'])
        exercise_angina = st.radio('Exercise Angina',['Yes','No'])
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