import streamlit as st
from streamlit_navigation_bar import st_navbar

import pages as pg
st.set_page_config(initial_sidebar_state="collapsed")

options = {
    "show_menu": False,
    "show_sidebar": False,
}

page= st_navbar(["Introdução", "Análise por Gênero", "Análise por Idade", "Indicadores","Metodologia", "Conclusão", "Referências" ], 
                      options=options)



functions = {
    "Introdução" : pg.show_introducao,
    "Referências": pg.show_referencias,
    "Metodologia" : pg.show_metodologia,
    "Análise por Gênero"    : pg.show_analise_por_genero,
    "Análise por Idade"     : pg.show_analise_por_idade,
    "Indicadores" : pg.show_indicadores,
    "Conclusão" : pg.show_conclusao
}


go_to = functions.get(page)

if go_to:
    go_to()