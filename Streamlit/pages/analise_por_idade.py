import streamlit as st
from streamlit_navigation_bar import st_navbar
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

def show_analise_por_idade():
    st.write("Observamos que no ano de 2021 havia uma tendência na faixa etária atendida pela Passos Mágicos.\n " +
             "Tendo uma maior concentração dos alunos com idades entre 9 e 14 anos.")

    show_1()   
    st.write("No ano de 2022 temos uma alteração nessa concentração, indo para o intervalo de 8 à 12 anos.")
    show_2()
    st.write("A partir de 2023 vemos que há uma tendência no atendimento aos alunos mais jovens, mudando a concentração para alunos com idade entre 6 e 12 anos.")
    show_3()
    st.write("Em 2024, essa tendência se manteve, com uma maior concentração de alunos com idades de 6 à 9 anos.")
    show_4()
    st.write("Com isso, vemos que a ong têm tido um aumento no atendimento à crianças da terceira infância.")
    st.write("Essa idade é muito importante, pois de acordo com Jean Piaget, nesse intervalo de idade as crianças começam a compreender conceitos lógicos e também são capazes de realizar tarefas mais complexas e entender relações de causa e consequência. ")
    st.write("Além disso, acredita-se que nessa idadeas crianças começama se sentir mais independentes, formando suas próprias ideias sobre o que é certo e errado.")
    st.write("Indo ao encontro do trabalho do psicólogo Albert Bandura, os comportamentos também podem ser aprendidos através da observação e modelagem. Ao observar as ações dos outros, incluindo pais e colegas, as crianças desenvolvem novas habilidades e adquirem novas informações.")
    st.write("Com isso, nota-se que é muito importante o atendimento à crianças de 6 à 12 anos, pois com uma melhor influência podem não se limitar às possibilidades oferecidas em um ambiente de vulnerabilidade social.")

def show_1():    
    dt = pd.read_csv("alunoPorIdade2021.csv", sep = ';')
    bar_1 = go.Bar(
        x = dt['IDADE'],
        y = dt['ALUNO_POR_IDADE'],
        name='Genero'

    )
    
    layout = go.Layout(
        title = "Alunos x Idade",
        xaxis= {'title':'Idade'},
        yaxis={'title':'Quantidade de Alunos'}
    )

    fig = go.Figure(data=bar_1, layout=layout)
    st.plotly_chart(fig)

def show_2():
    dt = pd.read_csv("alunoPorIdade2022.csv", sep = ';')
    bar_1 = go.Bar(
        x = dt['IDADE'],
        y = dt['ALUNO_POR_IDADE'],
        name='Genero'

    )
    
    layout = go.Layout(
        title = "Alunos x Idade",
        xaxis= {'title':'Idade'},
        yaxis={'title':'Quantidade de Alunos'}
    )

    fig = go.Figure(data=bar_1, layout=layout)
    st.plotly_chart(fig)

def show_3():
    dt = pd.read_csv("alunoPorIdade2023.csv", sep = ';')
    bar_1 = go.Bar(
        x = dt['IDADE'],
        y = dt['ALUNO_POR_IDADE'],
        name='Genero'

    )
    
    layout = go.Layout(
        title = "Alunos x Idade",
        xaxis= {'title':'Idade'},
        yaxis={'title':'Quantidade de Alunos'}
    )

    fig = go.Figure(data=bar_1, layout=layout)
    st.plotly_chart(fig)

def show_4():
    dt = pd.read_csv("alunoPorIdade2024.csv", sep = ';')
    bar_1 = go.Bar(
        x = dt['IDADE'],
        y = dt['ALUNO_POR_IDADE'],
        name='Genero'

    )
    
    layout = go.Layout(
        title = "Alunos x Idade",
        xaxis= {'title':'Idade'},
        yaxis={'title':'Quantidade de Alunos'}
    )

    fig = go.Figure(data=bar_1, layout=layout)
    st.plotly_chart(fig)    