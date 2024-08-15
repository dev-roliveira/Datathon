import streamlit as st
from streamlit_navigation_bar import st_navbar


def show_introducao():
    st.title("Introdução")
    st.write("A Associação Passos Mágicos é um Projeto da cidade de Embu Guaçu – SP. " +
            "\n\n Ela atua na transformação da vida de crianças e jovens de baixa renda, que encontram pela associação, melhores oportunidades de vida.")
    st.write("Dentre as atividades oferecidas pelo programa, os alunos possuem educação de qualidade, auxílio psicológico e psicopedagógico, " + 
            "ampliação da sua visão de mundo e protagonismo. Esse projeto social e educacional tem sido a porta de entrada para muitos jovens no ensino superior, " +
            "a partir de parcerias com universidades. Bem como parceria com escolas onde são oferecidas bolsas de estudo para os alunos além de terem tido a oportunidade de realizar um intercâmbio para Toronto.")
    st.write("Um estudo de 2023 feito pela UNICEF mostrou que mais de 60% da população brasileira até 17 anos vivem na pobreza.")
    st.write("Indo ao encontro desse estudo, em fevereiro de 2024 41,8% da população no estado de São Paulo estava em situação de pobreza, de acordo com o CadUnico.")
    st.write("Ainda segundo o levantamento, 66,3% das pessoas estão situadas na faixa de até um salario minimo.")
    st.write("De acordo com o mesmo levantamento, sobre a cidade de Embu-Guaçu,  vemos que 46% da população estão em situação de pobreza, 16% de famílias de baixa renda e 37% recebem acima de ½ salario minimo.")