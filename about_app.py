import streamlit as st
import pandas as pd

def run_about_app():
    st.header('Definição do Problema')
    st.text('Doenças cardiovasculares são a causa número 1 de morte global,\n' \
        'afetando mais de 17,9 milhões de pessoas anualmente, \n' \
        'que representa 31% das mortes em todo o planeta. \n' \
        'a cada 5 mortes por Doenças Cardiovasculares, 4 são de ataques cardíacos, \n' \
        'e cerca de 1/3 delas são em pessoas com menos de 70 anos de idade. \n'   )

    st.header('Objetivo')
    st.text('Dado que há diversos fatores de risco que podem contribuir para a \n' \
        'aparição de problemas cardíacos, pode-se estimar se os fatores estão \n' \
        'apontando alguma possibilidade de doença cardiovascular. \n' \
        'Portanto, nosso objetivo será construir um modelo de Machine Learning \n' \
        'que seja capaz de rotular um prognóstico para um paciente com \n' \
        'base nas informações clínicas fornecida')

    