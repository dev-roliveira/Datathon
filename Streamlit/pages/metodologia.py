import streamlit as st
from streamlit_navigation_bar import st_navbar


def show_metodologia():
        st.write("Para realizar as análises, foram criadas tabelas em um container Docker com uma base Oracle, baseadas nas informações disponibilizadas pelos arquivos compartilhados.")
        st.write("Com isso, foram feitas as análises através do DBeaver e exportados os resultados como arquivos de extensão csv, a fim de facilitar o upload para o GitHub posteriormente.")
        st.write("Foi escolhido o banco Oracle, devido à experiência e facilidade para a análise, se comparado à scrips em Python.")
        st.write("Abaixo, pode-se encontrar os scripts de banco utilizados para os cálculos e análises de dados.")
        with st.expander("Análise por Gênero"):
                st.title("Análise por Gênero")
                st.write("Porcentagem de público atendido por Gênero")
                st.code("SELECT \n" +
                        "Sexo, \n" +
                        "ROUND((COUNT(Sexo) / (SELECT COUNT(Sexo) FROM DATATHON_TBALUNO WHERE Sexo IS NOT NULL)) * 100, 2) AS Porcentagem \n" +
                        "FROM DATATHON_TBALUNO t \n" +
                        "WHERE Sexo IS NOT NULL \n" +
                        "GROUP BY Sexo;", language='sql')
                st.write("\n Evolução de Alunos por Gênero")
                st.code("SELECT\n" + 
                        "ANO,\n" +
                        "GENERO,\n" +
                        "COUNT(GENERO) AS TOTAL\n" +
                        "FROM (\n" +
                                "SELECT \n" +
                                "ALUNO.Sexo AS GENERO, \n" +
                                "TRUNC(TO_DATE(DIARIO_AULA.DataAula , 'YYYY-MM-DD HH24:MI:SS'), 'YYYY') AS ANO \n"+
                                "FROM DATATHON_TBALUNO ALUNO \n" +
                                "INNER JOIN DATATHON_TBDIARIOALUNO DIARIO_ALUNO ON ALUNO.IdAluno = DIARIO_ALUNO.IdAluno \n" +
                                "INNER JOIN DATATHON_TBDIARIOAULA DIARIO_AULA ON DIARIO_ALUNO.IdDiario = DIARIO_AULA.IdDiario \n" + 
                                "GROUP BY \n"+ 
                                "ALUNO.IdAluno, \n" +
                                "TRUNC(TO_DATE(DIARIO_AULA.DataAula , 'YYYY-MM-DD HH24:MI:SS'), 'YYYY'), \n" +
                                "ALUNO.Sexo) \n" +
                        "GROUP BY ANO, GENERO \n" +
                        "ORDER BY 1,2", language='sql')    
        with st.expander("Análise por Idade"):
                st.title("Análise por Idade")
                st.write("Alunos x Idade - 2021")
                st.code("SELECT \n"+
                        "COUNT(IDALUNO) AS ALUNO_POR_IDADE, \n" + 
                        "ROUND((TRUNC(TO_DATE('2021', 'YYYY'),'YYYY') - TRUNC(DTNASC, 'YYYY'))/365, 1) AS IDADE \n" +
                        "FROM ( \n"+
                                "SELECT \n" +   
                                "TRUNC(TO_DATE(ALUNO.DataNascimento , 'YYYY-MM-DD HH24:MI:SS'), 'YYYY') AS DTNASC, \n" +
                                "ALUNO.IdAluno  AS IDALUNO \n" +
                                "FROM DATATHON_TBALUNO ALUNO \n" +
                                "INNER JOIN DATATHON_TBDIARIOALUNO DIARIO_ALUNO ON ALUNO.IdAluno = DIARIO_ALUNO.IdAluno \n" + 
                                "INNER JOIN DATATHON_TBDIARIOAULA DIARIO_AULA ON DIARIO_ALUNO.IdDiario = DIARIO_AULA.IdDiario \n" +
                                "WHERE TRUNC(TO_DATE(DIARIO_AULA.DataAula, 'YYYY-MM-DD HH24:MI:SS'), 'YYYY')= '01/01/2021' \n" +
                                "GROUP BY  TRUNC(TO_DATE(ALUNO.DataNascimento, 'YYYY-MM-DD HH24:MI:SS'), 'YYYY'),ALUNO.IdAluno \n" +
                                ") GROUP BY DTNASC \n"+
                                "ORDER BY 2;",language='sql')
                st.write("Alunos x Idade - 2022")
                st.code("SELECT \n"+
                        "COUNT(IDALUNO) AS ALUNO_POR_IDADE, \n" + 
                        "ROUND((TRUNC(TO_DATE('2022', 'YYYY'),'YYYY') - TRUNC(DTNASC, 'YYYY'))/365, 1) AS IDADE \n" +
                        "FROM ( \n"+
                                "SELECT \n" +   
                                "TRUNC(TO_DATE(ALUNO.DataNascimento , 'YYYY-MM-DD HH24:MI:SS'), 'YYYY') AS DTNASC, \n" +
                                "ALUNO.IdAluno  AS IDALUNO \n" +
                                "FROM DATATHON_TBALUNO ALUNO \n" +
                                "INNER JOIN DATATHON_TBDIARIOALUNO DIARIO_ALUNO ON ALUNO.IdAluno = DIARIO_ALUNO.IdAluno \n" + 
                                "INNER JOIN DATATHON_TBDIARIOAULA DIARIO_AULA ON DIARIO_ALUNO.IdDiario = DIARIO_AULA.IdDiario \n" +
                                "WHERE TRUNC(TO_DATE(DIARIO_AULA.DataAula, 'YYYY-MM-DD HH24:MI:SS'), 'YYYY')= '01/01/2022' \n" +
                                "GROUP BY  TRUNC(TO_DATE(ALUNO.DataNascimento, 'YYYY-MM-DD HH24:MI:SS'), 'YYYY'),ALUNO.IdAluno \n" +
                                ") GROUP BY DTNASC \n"+
                                "ORDER BY 2;",language='sql')
                st.write("Alunos x Idade - 2023")
                st.code("SELECT \n"+
                        "COUNT(IDALUNO) AS ALUNO_POR_IDADE, \n" + 
                        "ROUND((TRUNC(TO_DATE('2023', 'YYYY'),'YYYY') - TRUNC(DTNASC, 'YYYY'))/365, 1) AS IDADE \n" +
                        "FROM ( \n"+
                                "SELECT \n" +   
                                "TRUNC(TO_DATE(ALUNO.DataNascimento , 'YYYY-MM-DD HH24:MI:SS'), 'YYYY') AS DTNASC, \n" +
                                "ALUNO.IdAluno  AS IDALUNO \n" +
                                "FROM DATATHON_TBALUNO ALUNO \n" +
                                "INNER JOIN DATATHON_TBDIARIOALUNO DIARIO_ALUNO ON ALUNO.IdAluno = DIARIO_ALUNO.IdAluno \n" + 
                                "INNER JOIN DATATHON_TBDIARIOAULA DIARIO_AULA ON DIARIO_ALUNO.IdDiario = DIARIO_AULA.IdDiario \n" +
                                "WHERE TRUNC(TO_DATE(DIARIO_AULA.DataAula, 'YYYY-MM-DD HH24:MI:SS'), 'YYYY')= '01/01/2023' \n" +
                                "GROUP BY  TRUNC(TO_DATE(ALUNO.DataNascimento, 'YYYY-MM-DD HH24:MI:SS'), 'YYYY'),ALUNO.IdAluno \n" +
                                ") GROUP BY DTNASC \n"+
                                "ORDER BY 2;",language='sql')    
                st.write("Alunos x Idade - 2024")
                st.code("SELECT \n"+
                        "COUNT(IDALUNO) AS ALUNO_POR_IDADE, \n" + 
                        "ROUND((TRUNC(TO_DATE('2024', 'YYYY'),'YYYY') - TRUNC(DTNASC, 'YYYY'))/365, 1) AS IDADE \n" +
                        "FROM ( \n"+
                                "SELECT \n" +   
                                "TRUNC(TO_DATE(ALUNO.DataNascimento , 'YYYY-MM-DD HH24:MI:SS'), 'YYYY') AS DTNASC, \n" +
                                "ALUNO.IdAluno  AS IDALUNO \n" +
                                "FROM DATATHON_TBALUNO ALUNO \n" +
                                "INNER JOIN DATATHON_TBDIARIOALUNO DIARIO_ALUNO ON ALUNO.IdAluno = DIARIO_ALUNO.IdAluno \n" + 
                                "INNER JOIN DATATHON_TBDIARIOAULA DIARIO_AULA ON DIARIO_ALUNO.IdDiario = DIARIO_AULA.IdDiario \n" +
                                "WHERE TRUNC(TO_DATE(DIARIO_AULA.DataAula, 'YYYY-MM-DD HH24:MI:SS'), 'YYYY')= '01/01/2024' \n" +
                                "GROUP BY  TRUNC(TO_DATE(ALUNO.DataNascimento, 'YYYY-MM-DD HH24:MI:SS'), 'YYYY'),ALUNO.IdAluno \n" +
                                ") GROUP BY DTNASC \n"+
                                "ORDER BY 2;",language='sql')   
        with st.expander("Análise Indicador de Autoavaliação"):
                st.title("IAA") 
                st.write("Indicador de Autoavaliação - 2020, 2021 e 2022")
                st.code("SELECT \n" +
                        "TIPO, \n" +
                        "COUNT(TIPO) AS TOTAL FROM ( \n "+
                                "SELECT \n" + 
                                "CASE WHEN IAA_2020 < IAA_2022 THEN 'EVOLUCAO' \n" + 
                                "WHEN IAA_2020 > IAA_2022 THEN 'REGRESSAO' \n" +
                                "ELSE 'MANTEVE' END AS TIPO \n" +
                                "FROM DATASET_DATATHON dd \n" + 
                                "WHERE \n" + 
                                "IAA_2020 IS NOT NULL AND \n" + 
                                "IAA_2021 IS NOT NULL AND \n" +
                                "IAA_2022 IS NOT NULL) \n" +
                                "GROUP BY TIPO;"
                                )
                st.write("Indicador de Autoavaliação - 2021 e 2022")
                st.code("SELECT \n" +
                        "TIPO, \n" +
                        "COUNT(TIPO) AS TOTAL FROM ( \n "+
                                "SELECT \n" + 
                                "CASE WHEN IAA_2021 < IAA_2022 THEN 'EVOLUCAO' \n" + 
                                "WHEN IAA_2021 > IAA_2022 THEN 'REGRESSAO' \n" +
                                "ELSE 'MANTEVE' END AS TIPO \n" +
                                "FROM DATASET_DATATHON dd \n" + 
                                "WHERE \n" + 
                                "IAA_2020 IS NULL AND \n" + 
                                "IAA_2021 IS NOT NULL AND \n" +
                                "IAA_2022 IS NOT NULL) \n" +
                                "GROUP BY TIPO;"
                                )
                st.write("Indicador de Autoavaliação - 2020 e 2021")
                st.code("SELECT \n" +
                        "TIPO, \n" +
                        "COUNT(TIPO) AS TOTAL FROM ( \n "+
                                "SELECT \n" + 
                                "CASE WHEN IAA_2020 < IAA_2021 THEN 'EVOLUCAO' \n" + 
                                "WHEN IAA_2020 > IAA_2021 THEN 'REGRESSAO' \n" +
                                "ELSE 'MANTEVE' END AS TIPO \n" +
                                "FROM DATASET_DATATHON dd \n" + 
                                "WHERE \n" + 
                                "IAA_2020 IS NOT NULL AND \n" + 
                                "IAA_2021 IS NOT NULL AND \n" +
                                "IAA_2022 IS NULL) \n" +
                                "GROUP BY TIPO;"
                                )        
        with st.expander("Análise Indicador Psicossocial - IPS"):
                st.title("IPS") 
                st.write("Indicador Psicossocial - 2020, 2021 e 2022")
                st.code("SELECT \n" +
                        "TIPO, \n" +
                        "COUNT(TIPO) AS TOTAL FROM ( \n "+
                                "SELECT \n" + 
                                "CASE WHEN IPS_2020 < IPS_2022 THEN 'EVOLUCAO' \n" + 
                                "WHEN IPS_2020 > IPS_2022 THEN 'REGRESSAO' \n" +
                                "ELSE 'MANTEVE' END AS TIPO \n" +
                                "FROM DATASET_DATATHON dd \n" + 
                                "WHERE \n" + 
                                "IPS_2020 IS NOT NULL AND \n" + 
                                "IPS_2021 IS NOT NULL AND \n" +
                                "IPS_2022 IS NOT NULL) \n" +
                                "GROUP BY TIPO;"
                                )
                st.write("Indicador Psicossocial - 2021 e 2022")
                st.code("SELECT \n" +
                        "TIPO, \n" +
                        "COUNT(TIPO) AS TOTAL FROM ( \n "+
                                "SELECT \n" + 
                                "CASE WHEN IPS_2021 < IPS_2022 THEN 'EVOLUCAO' \n" + 
                                "WHEN IPS_2021 > IPS_2022 THEN 'REGRESSAO' \n" +
                                "ELSE 'MANTEVE' END AS TIPO \n" +
                                "FROM DATASET_DATATHON dd \n" + 
                                "WHERE \n" + 
                                "IPS_2020 IS NULL AND \n" + 
                                "IPS_2021 IS NOT NULL AND \n" +
                                "IPS_2022 IS NOT NULL) \n" +
                                "GROUP BY TIPO;"
                                )
                st.write("Indicador Psicossocial - 2020 e 2021")
                st.code("SELECT \n" +
                        "TIPO, \n" +
                        "COUNT(TIPO) AS TOTAL FROM ( \n "+
                                "SELECT \n" + 
                                "CASE WHEN IPS_2020 < IPS_2021 THEN 'EVOLUCAO' \n" + 
                                "WHEN IPS_2020 > IPS_2021 THEN 'REGRESSAO' \n" +
                                "ELSE 'MANTEVE' END AS TIPO \n" +
                                "FROM DATASET_DATATHON dd \n" + 
                                "WHERE \n" + 
                                "IPS_2020 IS NOT NULL AND \n" + 
                                "IPS_2021 IS NOT NULL AND \n" +
                                "IPS_2022 IS NULL) \n" +
                                "GROUP BY TIPO;"
                                )              
        with st.expander("Análise Indicador Psicopedagógico - IPP"):
                st.title("IPP") 
                st.write("Indicador Psicopedagógico - 2020, 2021 e 2022")
                st.code("SELECT \n" +
                        "TIPO, \n" +
                        "COUNT(TIPO) AS TOTAL FROM ( \n "+
                                "SELECT \n" + 
                                "CASE WHEN IPP_2020 < IPP_2022 THEN 'EVOLUCAO' \n" + 
                                "WHEN IPP_2020 > IPP_2022 THEN 'REGRESSAO' \n" +
                                "ELSE 'MANTEVE' END AS TIPO \n" +
                                "FROM DATASET_DATATHON dd \n" + 
                                "WHERE \n" + 
                                "IPP_2020 IS NOT NULL AND \n" + 
                                "IPP_2021 IS NOT NULL AND \n" +
                                "IPP_2022 IS NOT NULL) \n" +
                                "GROUP BY TIPO;"
                                )
                st.write("Indicador Psicopedagógico - 2021 e 2022")
                st.code("SELECT \n" +
                        "TIPO, \n" +
                        "COUNT(TIPO) AS TOTAL FROM ( \n "+
                                "SELECT \n" + 
                                "CASE WHEN IPP_2021 < IPP_2022 THEN 'EVOLUCAO' \n" + 
                                "WHEN IPP_2021 > IPP_2022 THEN 'REGRESSAO' \n" +
                                "ELSE 'MANTEVE' END AS TIPO \n" +
                                "FROM DATASET_DATATHON dd \n" + 
                                "WHERE \n" + 
                                "IPP_2020 IS NULL AND \n" + 
                                "IPP_2021 IS NOT NULL AND \n" +
                                "IPP_2022 IS NOT NULL) \n" +
                                "GROUP BY TIPO;"
                                )
                st.write("Indicador Psicopedagógico - 2020 e 2021")
                st.code("SELECT \n" +
                        "TIPO, \n" +
                        "COUNT(TIPO) AS TOTAL FROM ( \n "+
                                "SELECT \n" + 
                                "CASE WHEN IPP_2020 < IPP_2021 THEN 'EVOLUCAO' \n" + 
                                "WHEN IPP_2020 > IPP_2021 THEN 'REGRESSAO' \n" +
                                "ELSE 'MANTEVE' END AS TIPO \n" +
                                "FROM DATASET_DATATHON dd \n" + 
                                "WHERE \n" + 
                                "IPP_2020 IS NOT NULL AND \n" + 
                                "IPP_2021 IS NOT NULL AND \n" +
                                "IPP_2022 IS NULL) \n" +
                                "GROUP BY TIPO;"
                                )                   
        with st.expander("Análise Indicador de Engajamento - IEG"):
                st.title("IEG") 
                st.write("Indicador de Engajamento - 2020, 2021 e 2022")
                st.code("SELECT \n" +
                        "TIPO, \n" +
                        "COUNT(TIPO) AS TOTAL FROM ( \n "+
                                "SELECT \n" + 
                                "CASE WHEN IEG_2020 < IEG_2022 THEN 'EVOLUCAO' \n" + 
                                "WHEN IEG_2020 > IEG_2022 THEN 'REGRESSAO' \n" +
                                "ELSE 'MANTEVE' END AS TIPO \n" +
                                "FROM DATASET_DATATHON dd \n" + 
                                "WHERE \n" + 
                                "IEG_2020 IS NOT NULL AND \n" + 
                                "IEG_2021 IS NOT NULL AND \n" +
                                "IEG_2022 IS NOT NULL) \n" +
                                "GROUP BY TIPO;"
                                )
                st.write("Indicador de Engajamento - 2021 e 2022")
                st.code("SELECT \n" +
                        "TIPO, \n" +
                        "COUNT(TIPO) AS TOTAL FROM ( \n "+
                                "SELECT \n" + 
                                "CASE WHEN IEG_2021 < IEG_2022 THEN 'EVOLUCAO' \n" + 
                                "WHEN IEG_2021 > IEG_2022 THEN 'REGRESSAO' \n" +
                                "ELSE 'MANTEVE' END AS TIPO \n" +
                                "FROM DATASET_DATATHON dd \n" + 
                                "WHERE \n" + 
                                "IEG_2020 IS NULL AND \n" + 
                                "IEG_2021 IS NOT NULL AND \n" +
                                "IEG_2022 IS NOT NULL) \n" +
                                "GROUP BY TIPO;"
                                )
                st.write("Indicador de Engajamento - 2020 e 2021")
                st.code("SELECT \n" +
                        "TIPO, \n" +
                        "COUNT(TIPO) AS TOTAL FROM ( \n "+
                                "SELECT \n" + 
                                "CASE WHEN IEG_2020 < IEG_2021 THEN 'EVOLUCAO' \n" + 
                                "WHEN IEG_2020 > IEG_2021 THEN 'REGRESSAO' \n" +
                                "ELSE 'MANTEVE' END AS TIPO \n" +
                                "FROM DATASET_DATATHON dd \n" + 
                                "WHERE \n" + 
                                "IEG_2020 IS NOT NULL AND \n" + 
                                "IEG_2021 IS NOT NULL AND \n" +
                                "IEG_2022 IS NULL) \n" +
                                "GROUP BY TIPO;"
                                )                                              
        with st.expander("Análise Indicador de Desempenho Acadêmico - IDA"):
                st.title("IDA") 
                st.write("Indicador de Desempenho Acadêmico - 2020, 2021 e 2022")
                st.code("SELECT \n" +
                        "TIPO, \n" +
                        "COUNT(TIPO) AS TOTAL FROM ( \n "+
                                "SELECT \n" + 
                                "CASE WHEN IDA_2020 < IDA_2022 THEN 'EVOLUCAO' \n" + 
                                "WHEN IDA_2020 > IDA_2022 THEN 'REGRESSAO' \n" +
                                "ELSE 'MANTEVE' END AS TIPO \n" +
                                "FROM DATASET_DATATHON dd \n" + 
                                "WHERE \n" + 
                                "IDA_2020 IS NOT NULL AND \n" + 
                                "IDA_2021 IS NOT NULL AND \n" +
                                "IDA_2022 IS NOT NULL) \n" +
                                "GROUP BY TIPO;"
                                )
                st.write("Indicador de Desempenho Acadêmico - 2021 e 2022")
                st.code("SELECT \n" +
                        "TIPO, \n" +
                        "COUNT(TIPO) AS TOTAL FROM ( \n "+
                                "SELECT \n" + 
                                "CASE WHEN IDA_2021 < IDA_2022 THEN 'EVOLUCAO' \n" + 
                                "WHEN IDA_2021 > IDA_2022 THEN 'REGRESSAO' \n" +
                                "ELSE 'MANTEVE' END AS TIPO \n" +
                                "FROM DATASET_DATATHON dd \n" + 
                                "WHERE \n" + 
                                "IDA_2020 IS NULL AND \n" + 
                                "IDA_2021 IS NOT NULL AND \n" +
                                "IDA_2022 IS NOT NULL) \n" +
                                "GROUP BY TIPO;"
                                )
                st.write("Indicador de Desempenho Acadêmico - 2020 e 2021")
                st.code("SELECT \n" +
                        "TIPO, \n" +
                        "COUNT(TIPO) AS TOTAL FROM ( \n "+
                                "SELECT \n" + 
                                "CASE WHEN IDA_2020 < IDA_2021 THEN 'EVOLUCAO' \n" + 
                                "WHEN IDA_2020 > IDA_2021 THEN 'REGRESSAO' \n" +
                                "ELSE 'MANTEVE' END AS TIPO \n" +
                                "FROM DATASET_DATATHON dd \n" + 
                                "WHERE \n" + 
                                "IDA_2020 IS NOT NULL AND \n" + 
                                "IDA_2021 IS NOT NULL AND \n" +
                                "IDA_2022 IS NULL) \n" +
                                "GROUP BY TIPO;"
                                )          
        with st.expander("Análise Indicador do Ponto de Virada - IPV"):
                st.title("IPV") 
                st.write("Indicador do Ponto de Virada- 2020")
                st.code("SELECT \n" +
                        "PONTO_VIRADA_2020, \n" +
                        "COUNT(PONTO_VIRADA_2020) AS TOTAL ( \n "+
                                "FROM ( \n" + 
                                "SELECT' \n" + 
                                "CASE WHEN PONTO_VIRADA_2020 = 'Sim' THEN 'Manteve'' \n" +
                                "	 WHEN PONTO_VIRADA_2020 = 'Não' THEN 'Evoluiu' END AS PONTO_VIRADA_2020,  \n" +
                                "CASE WHEN PONTO_VIRADA_2021 = 'Sim' THEN 'Manteve' \n" + 
                                "	 WHEN PONTO_VIRADA_2021 = 'Não' THEN 'Evoluiu' END AS PONTO_VIRADA_2021, \n" + 
                                "CASE WHEN PONTO_VIRADA_2022 = 'Sim' THEN 'Manteve' \n" + 
                                "	 WHEN PONTO_VIRADA_2022 = 'Não' THEN 'Evoluiu' END AS PONTO_VIRADA_2022   \n" +
                                "FROM DATASET_DATATHON dd \n" +
                                "WHERE \n" +
                                "PONTO_VIRADA_2020 IS NOT NULL AND \n" +
                                "PONTO_VIRADA_2021 IS NOT NULL AND \n" +
                                "PONTO_VIRADA_2022 IS NOT NULL) \n" +
                                "GROUP BY PONTO_VIRADA_2020;"
                                )
                st.write("Indicador do Ponto de Virada- 2021")
                st.code("SELECT \n" +
                        "PONTO_VIRADA_2021, \n" +
                        "COUNT(PONTO_VIRADA_2021) AS TOTAL ( \n "+
                                "FROM ( \n" + 
                                "SELECT' \n" + 
                                "CASE WHEN PONTO_VIRADA_2020 = 'Sim' THEN 'Manteve'' \n" +
                                "	 WHEN PONTO_VIRADA_2020 = 'Não' THEN 'Evoluiu' END AS PONTO_VIRADA_2020,  \n" +
                                "CASE WHEN PONTO_VIRADA_2021 = 'Sim' THEN 'Manteve' \n" + 
                                "	 WHEN PONTO_VIRADA_2021 = 'Não' THEN 'Evoluiu' END AS PONTO_VIRADA_2021, \n" + 
                                "CASE WHEN PONTO_VIRADA_2022 = 'Sim' THEN 'Manteve' \n" + 
                                "	 WHEN PONTO_VIRADA_2022 = 'Não' THEN 'Evoluiu' END AS PONTO_VIRADA_2022   \n" +
                                "FROM DATASET_DATATHON dd \n" +
                                "WHERE \n" +
                                "PONTO_VIRADA_2020 IS NOT NULL AND \n" +
                                "PONTO_VIRADA_2021 IS NOT NULL AND \n" +
                                "PONTO_VIRADA_2022 IS NOT NULL) \n" +
                                "GROUP BY PONTO_VIRADA_2021;"
                                )
                st.write("Indicador do Ponto de Virada- 2022")
                st.code("SELECT \n" +
                        "PONTO_VIRADA_2022, \n" +
                        "COUNT(PONTO_VIRADA_2022) AS TOTAL ( \n "+
                                "FROM ( \n" + 
                                "SELECT' \n" + 
                                "CASE WHEN PONTO_VIRADA_2020 = 'Sim' THEN 'Manteve'' \n" +
                                "	 WHEN PONTO_VIRADA_2020 = 'Não' THEN 'Evoluiu' END AS PONTO_VIRADA_2020,  \n" +
                                "CASE WHEN PONTO_VIRADA_2021 = 'Sim' THEN 'Manteve' \n" + 
                                "	 WHEN PONTO_VIRADA_2021 = 'Não' THEN 'Evoluiu' END AS PONTO_VIRADA_2021, \n" + 
                                "CASE WHEN PONTO_VIRADA_2022 = 'Sim' THEN 'Manteve' \n" + 
                                "	 WHEN PONTO_VIRADA_2022 = 'Não' THEN 'Evoluiu' END AS PONTO_VIRADA_2022   \n" +
                                "FROM DATASET_DATATHON dd \n" +
                                "WHERE \n" +
                                "PONTO_VIRADA_2020 IS NOT NULL AND \n" +
                                "PONTO_VIRADA_2021 IS NOT NULL AND \n" +
                                "PONTO_VIRADA_2022 IS NOT NULL) \n" +
                                "GROUP BY PONTO_VIRADA_2022;"
                                )
        with st.expander("Indicador de Adequação de Nível - IAN"):
                st.title("IAN") 
                st.write("Indicador de Adequação de Nível - 2020, 2021 e 2022")
                st.code("SELECT \n" +
                        "TIPO, \n" +
                        "COUNT(TIPO) AS TOTAL FROM ( \n "+
                                "SELECT \n" + 
                                "CASE WHEN IAN_2020 < IAN_2022 THEN 'EVOLUCAO' \n" + 
                                "WHEN IAN_2020 > IAN_2022 THEN 'REGRESSAO' \n" +
                                "ELSE 'MANTEVE' END AS TIPO \n" +
                                "FROM DATASET_DATATHON dd \n" + 
                                "WHERE \n" + 
                                "IAN_2020 IS NOT NULL AND \n" + 
                                "IAN_2021 IS NOT NULL AND \n" +
                                "IAN_2022 IS NOT NULL) \n" +
                                "GROUP BY TIPO;"
                                )
                st.write("Indicador de Adequação de Nível - 2021 e 2022")
                st.code("SELECT \n" +
                        "TIPO, \n" +
                        "COUNT(TIPO) AS TOTAL FROM ( \n "+
                                "SELECT \n" + 
                                "CASE WHEN IAN_2021 < IAN_2022 THEN 'EVOLUCAO' \n" + 
                                "WHEN IAN_2021 > IAN_2022 THEN 'REGRESSAO' \n" +
                                "ELSE 'MANTEVE' END AS TIPO \n" +
                                "FROM DATASET_DATATHON dd \n" + 
                                "WHERE \n" + 
                                "IAN_2020 IS NULL AND \n" + 
                                "IAN_2021 IS NOT NULL AND \n" +
                                "IAN_2022 IS NOT NULL) \n" +
                                "GROUP BY TIPO;"
                                )
                st.write("Indicador de Adequação de Nível - 2020 e 2021")
                st.code("SELECT \n" +
                        "TIPO, \n" +
                        "COUNT(TIPO) AS TOTAL FROM ( \n "+
                                "SELECT \n" + 
                                "CASE WHEN IAN_2020 < IAN_2021 THEN 'EVOLUCAO' \n" + 
                                "WHEN IAN_2020 > IAN_2021 THEN 'REGRESSAO' \n" +
                                "ELSE 'MANTEVE' END AS TIPO \n" +
                                "FROM DATASET_DATATHON dd \n" + 
                                "WHERE \n" + 
                                "IAN_2020 IS NOT NULL AND \n" + 
                                "IAN_2021 IS NOT NULL AND \n" +
                                "IAN_2022 IS NULL) \n" +
                                "GROUP BY TIPO;"
                                )          