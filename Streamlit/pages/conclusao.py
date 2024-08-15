import streamlit as st
from streamlit_navigation_bar import st_navbar
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

def show_conclusao():
    st.write("Com a análise dos dados fornecidos, vemos que a Associação Passos Mágicos têm uma grande importância para as crianças e jovens em sua região.")
    st.write("Com o objetivo principal de distanciá-los da situação de vulnerabilidade social e dispertar a importância da educação para o futuro da sociedade e deles como integrantes dessa sociedade.")
    st.write("Entretanto, a precisão dos dados compartilhados não foi muito alta. Faltaram ainda algumas relações que pudéssemos fazer, a fim de ter uma maior observabilidade do todo.")
    st.write("Acredito que futuramente, possa ser visto a possibilidade de compartilhar o banco de dados anonimizado com os diagramas e assim facilitar a relação entre as informações e tabelas.")
    st.write("Talvez com esse melhor planejamento para compartilhamento dos dados, com maior antecedência e mais clareza possa aumentar as possibilidades de análises a fim de conseguirmos auxiliar a instituição.")
    st.write("Uma comparação simples, sobre a inconsistência dos dados, por exemplo é que se filtrarmos os alunos que tiveram algum registro de aula no ano de 2021 totalizam 790 alunos. Entretanto, se vermos os alunos da primeira base de dados, esse número cai para 686.")