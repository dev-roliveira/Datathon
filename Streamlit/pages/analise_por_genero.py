import streamlit as st
from streamlit_navigation_bar import st_navbar
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

def show_analise_por_genero():
    st.write("Com os dados analisados de 2021 até 2024, observa-se que 53,64% do público atendido é do Gênero Feminino a Passos Mágicos. \n\n"
             + "O que acaba indo ao encontro do censo de 2022, que nos mostrou que 51,5% da população brasileira é composta por mulheres.")

    show_1()   
    st.write("Analisando ainda a evolução anual dessa proporção, obtemos o seguinte gráfico:")
    show_2()

def show_1():    
    dt = pd.read_csv("https://raw.githubusercontent.com/dev-roliveira/Datathon/master/Streamlit/generoTotal.csv", sep = ';')
    bar_1 = go.Bar(
        x = dt['Sexo'],
        y = dt['Porcentagem'],
        name='Genero'

    )
    
    layout = go.Layout(
        title = "Comparativo de Gênero",
        xaxis= {'title':'Genero'},
        yaxis={'title':'Porcentagem'}
    )

    fig = go.Figure(data=bar_1, layout=layout)
    st.plotly_chart(fig)

def show_2():
    dt = pd.read_csv("https://raw.githubusercontent.com/dev-roliveira/Datathon/master/Streamlit/EvolucaoGeneroPorAno.csv", sep = ';')
    dt['ANO'] = pd.to_datetime(dt['ANO']).dt.year

    fig = px.bar(dt, x=dt['ANO'], y=dt['TOTAL'], color=dt['GENERO'], title="Evolução de Alunos por Gênero")
    fig.update_layout(xaxis = dict(
                    tickmode='array', #change 1
                    tickvals = dt['ANO'], #change 2
                    ),
                   font=dict(size=18, color="black"))
    st.plotly_chart(fig)
