import streamlit as st
import streamlit.components.v1 as stc

from eda_app import *
from ml_app import *
from about_app import *

html_temp = """
		<div style="background-color:#3872fb;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Heart Disease Prediction </h1>
		</div>
		"""

def main():
    st.title('Main App')
    stc.html(html_temp)

    menu = ['Home','EDA','Predict Disease','About']
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'Home':
        st.header('Home')

        st.subheader('Sobre')
        st.text('Esta aplicação retorna um prognóstico para doenças cardiovasculares \n' \
            'baseado nas informações clínicas de um determinado paciente')

        st.subheader('Definição do Problema')
        st.text('Doenças cardiovasculares são a causa número 1 de morte global,\n' \
            'afetando mais de 17,9 milhões de pessoas anualmente, \n' \
            'que representa 31% das mortes em todo o planeta. \n' \
            'a cada 5 mortes por Doenças Cardiovasculares, 4 são de ataques cardíacos, \n' \
            'e cerca de 1/3 delas são em pessoas com menos de 70 anos de idade. \n'   )

        st.subheader('Objetivo')
        st.text('Dado que há diversos fatores de risco que podem contribuir para a \n' \
            'aparição de problemas cardíacos, pode-se estimar se os fatores estão \n' \
            'apontando alguma possibilidade de doença cardiovascular. \n' \
            'Portanto, nosso objetivo será construir um modelo de Machine Learning \n' \
            'que seja capaz de rotular um prognóstico para um paciente com \n' \
            'base nas informações clínicas fornecida')

    elif choice == 'EDA':
        run_eda_app()
    elif choice ==  'Predict Disease':
        run_ml_app()
    elif choice == 'About':
        run_about_app()

if __name__ == '__main__':
    main()