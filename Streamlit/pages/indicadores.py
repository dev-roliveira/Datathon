import streamlit as st
import pandas as pd
import plotly.express as px

def show_indicadores():
    with st.expander("Indicador de Autoavaliação - IAA"):
        st.title("Indicador de Autoavaliação - IAA")
        st.write("O IAA é um indicador de avaliação psicossocial, onde seus resultados são produzidos pelo próprio estudante, a partir de respostas sobre ele mesmo a respeito de aspectos da sua vida e de sua experiência cotidiana.")
        st.write("")
        st.write("Analisando os resultados oferecidos, dos alunos que participaram da Passos Mágicos nos anos de 2020, 2021 e 2022 vemos que há uma diminuição na nota dos alunos.")
        st.write("54,46% dos alunos se avaliaram com notas menores se compararmos 2020 com 2022.")
        st.write("Além disso, somente 29,29% se avaliaram com notas maiores que a avaliação anterior, enquanto os demais mantiveram a mesma nota.")
        dt = pd.read_csv('IAA_2020_2022.csv', sep=';')
        fig = px.bar(data_frame=dt, x=dt['TIPO'], y=dt['TOTAL'])
        st.plotly_chart(fig)

        st.write("")
        st.write("Porém, se analisarmos os alunos que entraram em 2021, vemos que as avaliações possuem uma evolução quando comparamos com o IAA de 2022.")
        st.write("Comparando as notas das avaliações dos mesmos alunos, cerca de 52,45% aumentaram sua autoavaliação.")
        dt = pd.read_csv('IAA_2021_2022.csv', sep=';')
        fig = px.bar(data_frame=dt, x=dt['TIPO'], y=dt['TOTAL'])
        st.plotly_chart(fig)

        st.write("")
        st.write("Ao analisar os resultados do indicador, para alunos que participaram da instituição somente nos anos de 2020 e 2021, vemos que há uma diminuição na nota obtida.")
        st.write("Cerca de 62% dos alunos que responderam, tiveram notas menores em 2021 que se compararmos com as notas de 2020.")
        dt = pd.read_csv('IAA_2020_2021.csv', sep=';')
        fig = px.bar(data_frame=dt, x=dt['TIPO'], y=dt['TOTAL'])
        st.plotly_chart(fig)

        st.write("")
        st.write("Com isso vemos que apesar das notas de 2022 serem menores que as notas de 2020, se compararmos com os ingressantes de 2021 há uma evolução.")
        st.write("Talvez, isso deva ao fato de que os alunos com mais tempo de Instituição adquirem um melhor senso crítico, se sintam desmotivados, tenham mais entendimento sobre a sua relação familiar, se sintam pressionados em relação à si mesmos, dentre outros.")
        st.write("Contudo, para concluir precisamente sobre qual aspecto está regredindo nas avaliações, é necessário analisar os questionários respondidos e não somente as notas.")
   
    with st.expander("Indicador Psicossocial - IPS"):
        st.title("Indicador Psicossocial - IPS")
        st.write("Os resultados desse indicador foram obtidos por meio de avaliações feitas pela equipe de psicologia da Associação.")
        st.write("A avaliação é feita considerando quatro questões a serem analisadas pela equipe: ")
        st.write("Questão 1 - Percepção da equipe de psicologia quanto as dificuldades enfrentadas pelo estudante e sua família, na dinâmica da convivência familiar.")
        st.write("Questão 2 - Aspectos do desenvolvimento emocional dos estudantes.")
        st.write("Questão 3 - Comportamento do estudante.")
        st.write("Questão 4 - Dinâmica de socialização do estudante.")
        st.write("")
        st.write("A partir dos dados oferecidos, pode-se analisar que os estudantes que participaram da associação em todos os anos no intervalo de 2020 e 2022, tiveram 31,53% tiveram melhoria na sua avaliação.")
        st.write("Em contrapartida, 27,29% tiveram notas inferiores em relação à primeira avaliação. Enquanto os demais, mantiveram a mesma nota.")
        dt = pd.read_csv('IPS_2020_2022.csv', sep=';')
        fig = px.bar(data_frame=dt, x=dt['TIPO'], y=dt['TOTAL'])
        st.plotly_chart(fig)

        st.write("")
        st.write("Ao analisarmos os alunos que ingressaram em 2021, temos uma pequena melhora na evolução da avaliação. Nesse caso, 32,17% dos alunos tiveram em 2022 notas maiores que 2021.")
        st.write("Mas o destaque maior é para as notas que regrediram, onde apenas 9,09% tiveram essa situação. Os demais, mantiveram a nota do ano anterior.")
        dt = pd.read_csv('IPS_2021_2022.csv', sep=';')
        fig = px.bar(data_frame=dt, x=dt['TIPO'], y=dt['TOTAL'])
        st.plotly_chart(fig)

        st.write("")
        st.write("Se considerarmos os alunos que participaram somente nos anos de 2020 e 2021, vemos que as notas que regrediram foram superiores às notas que tiveram um aumento.")
        st.write("Cerca de 39,86% dos alunos tiveram notas em 2021 menores que as notas de 2020. E apenas 18,19% tiveram notas superiores se comparado ao ano anterior.")
        dt = pd.read_csv('IPS_2020_2021.csv', sep=';')
        fig = px.bar(data_frame=dt, x=dt['TIPO'], y=dt['TOTAL'])
        st.plotly_chart(fig)

        st.write("")
        st.write("Vemos que nos anos iniciais, os alunos que participaram somente nos anos de 2020 e 2021 tiveram uma regressão nas suas avaliações.")
        st.write("Ao analisarmos os alunos que estavam nos anos de 2021 e 2022, vemos que as notas que tiveram aumento são quase 2x maiores que as notas nos dois anos anteriores.")
        st.write("O mesmo acontece se vermos os alunos que participaram os três anos na Instituição, onde aproximadamente 32% dos alunos melhoraram suas avaliações.")
        st.write("Esse indicador é muito importante, pois podemos acompanhar a evolução dos alunos em uma avaliação feita por profissionais da área de psicologia da Passos Mágicos.")
        st.write("Infelizmente, sem o acesso aos questionários, não temos como saber e indicar qual aspecto teve melhoras ou piora no resultado final.")

    with st.expander("Indicador Psicopedagógico - IPP"):
        st.title("Indicador Psicopedagógico - IPP")  
        st.write("Assim como o IPS, o IPP é obtido a partir de avaliações individuais feitas por membros da equipe de professores e psicopedagogos da Associação Passos Mágicos.")
        st.write("O IPS avalia quatro aspectos do desenvolvimento psicopedagógico: desenvolvimento cognitivo, emocional, comportamental e de socialização.") 
        st.write("Os avaliadores caracterizam cada um dos aspectos respondendo qual condição descreve melhor o desenvolvimento atual.")
        
        st.write("")
        st.write("Seguindo a mesma ordem das análises anteriores, vemos que 44,59% dos alunos que participaram da Associação nos anos de 2020, 2021 e 2022 tiveram aumento na avaliação do IPP.")
        st.write("Além disso, 51,91% tiveram retrocesso nas avaliações.")
        dt = pd.read_csv('IPP_2020_2022.csv', sep=';')
        fig = px.bar(data_frame=dt, x=dt['TIPO'], y=dt['TOTAL'])
        st.plotly_chart(fig)

        st.write("")
        st.write("Ao compararmos os resultados dos alunos que entraram em 2021, vemos que 37,06% tiveram notas em 2022 superiores que as notas do ano anterior.")
        st.write("Entretanto, 61,54% tiveram diminuição em suas notas.")
        dt = pd.read_csv('IPP_2021_2022.csv', sep=';')
        fig = px.bar(data_frame=dt, x=dt['TIPO'], y=dt['TOTAL'])
        st.plotly_chart(fig)

        st.write("")
        st.write("O mesmo cenário se repete nos dados de 2020 e 2021, onde 41,96% das notas aumentaram após a primeira avaliação. E 55,94% diminuiram a nota de avaliação se comparado ao ano anterior")
        dt = pd.read_csv('IPP_2020_2021.csv', sep=';')
        fig = px.bar(data_frame=dt, x=dt['TIPO'], y=dt['TOTAL'])
        st.plotly_chart(fig)

    with st.expander("Indicador de Engajamento - IEG"):
        st.title("Indicador de Engajamento - IEG")
        st.write("Este indicador registra a participação dos alunos de universidade em ações de voluntariado e a entrega de lições de casa dos estudantes de fase escolar.")
        st.write("Infelizmente vemos uma grande regressão nos dados de alunos que participaram nos anos de 2020, 2021 e 2022. Cerca de 67,52% dos alunos tiveram diminuição nas suas notas enquanto 31,21% tiveram aumento.")
        dt = pd.read_csv('IEG_2020_2022.csv', sep=';')
        fig = px.bar(data_frame=dt, x=dt['TIPO'], y=dt['TOTAL'])
        st.plotly_chart(fig)

        st.write("")                
        st.write("O mesmo se repete para quem participou nos anos de 2021 e 2022, tendo 50,35% dos alunos sendo avaliados com notas inferiores que no primeiro ano.")
        dt = pd.read_csv('IEG_2021_2022.csv', sep=';')
        fig = px.bar(data_frame=dt, x=dt['TIPO'], y=dt['TOTAL'])
        st.plotly_chart(fig)

        st.write("")
        st.write("E para alunos que estava na Passos Mágicos nas avaliações de 2020 e 2021, vemos que 76,22% tiveram notas menores na segunda avaliação.")    
        dt = pd.read_csv('IEG_2020_2021.csv', sep=';')
        fig = px.bar(data_frame=dt, x=dt['TIPO'], y=dt['TOTAL'])
        st.plotly_chart(fig)

        st.write("")
        st.write("É preciso analisar com mais detalhamento e entender os motivos que fazem com que os estudantes não participem tanto do voluntariado, e também o motivo de não realizarem as lições de casa.")
        st.write("Este segundo ponto, pode ser motivacionado pelo desinteresse em casa por parte dos responsáveis em participar da vida escolar da criança.")
    
    with st.expander("Indicador de Desempenho Acadêmico - IDA"):
        st.title("Indicador de Desempenho Acadêmico - IDA")
        st.write("Este indicador é produzido a partir do resultado das provas de Português e Matemática, aplicadas a todas as Fases de Ensino da associação, e adicionalmente os resultados das provas de Ingês, aplicadas a partir da Fase 3, durante o ano letivo.")
        st.write("No caso dos alunos da Fase 8, esse indicador registra a nota média obtida pelos alunos em todas as disciplinas curriculares cursadas nas instituições de ensino superior.")
        st.write("Analisando as avaliações dos alunos que participaram da Associação nos anos de 2020 à 2022, observa-se que 74,20% dos alunos tiveram notas menores em 2022 que comparado às notas de 2020.")
    
        dt = pd.read_csv('IDA_2020_2022.csv', sep=';')
        fig = px.bar(data_frame=dt, x=dt['TIPO'], y=dt['TOTAL'])
        st.plotly_chart(fig)

        st.write("")                
        st.write("Porém, se analisarmos as avaliações de 2021 e 2022, desconsiderando quem não foi avaliado em 2020, vemos que 61,54% dos alunos tiveram uma melhoria das notas.")
        dt = pd.read_csv('IDA_2021_2022.csv', sep=';')
        fig = px.bar(data_frame=dt, x=dt['TIPO'], y=dt['TOTAL'])
        st.plotly_chart(fig)

        st.write("")
        st.write("E para alunos que estava na Passos Mágicos nas avaliações de 2020 e 2021, vemos que 67,13% tiveram notas menores na segunda avaliação.")    
        dt = pd.read_csv('IDA_2020_2021.csv', sep=';')
        fig = px.bar(data_frame=dt, x=dt['TIPO'], y=dt['TOTAL'])
        st.plotly_chart(fig)

        st.write("")
        st.write("Infelizmente vemos a mesma tendência que há nos outros indicadores, onde há uma diminuição nas notas ao passar dos anos dos alunos na instituição.")
        st.write("Acredito que uma análise mais aprofundada e detalhada nas avaliações, seja importante para que possam ser mapeadas as dificuldades e necessidades de cada aluno, a fim de terem um direcionamento personalizado.")
    
    with st.expander("Indicador do Ponto de Virada - IPV"):
        st.title("Indicador do Ponto de Virada - IPV")
        st.write("Este indicador é um dos mais importantes da Associação Passos Mágicos. Seus resultados são obtidos por meio de avaliações individuais, feitas por membros da equipe de professores e psicopedagogos da associação.")
        st.write("Este Ponto de Virada é um estágio do desenvolvimento do etudante, no qual ele demonstra de forma ativa, por meio da sua trajetória dentro da associação, estar consciente da importância da educação, do valor do saber e da importância de aprender.")
        st.write("Passar por esse ponto, significa que o aluno está apto a iniciar a transformação da sua vida por meio da educação.")  
        st.write("A avaliação do IPV foi feita analisando três aspectos do desenvolvimento do estudante: sua integração à associação, o seu desenvolvimento emocional e o seu potencial acadêmico.")

        st.write("Observamos que analisando os dados de alunos que participaram em 2020 cerca de 82,16% dos alunos tiveram essa mudança e conscientização da importância da educação.")  
        dt = pd.read_csv('IPV_2020.csv', sep=';')
        fig = px.bar(data_frame=dt, x=dt['PONTO_VIRADA_2020'], y=dt['TOTAL'])
        st.plotly_chart(fig)

        st.write("")                
        st.write("Analisando também os alunos que participaram das avaliações somente nos anos de 2021, temos essa mesma tendência. Onde 83,12% dos alunos atingiram o Ponto de Virada.")
        dt = pd.read_csv('IPV_2021.csv', sep=';')
        fig = px.bar(data_frame=dt, x=dt['PONTO_VIRADA_2021'], y=dt['TOTAL'])
        st.plotly_chart(fig)

        st.write("")
        st.write("E a mesma porcentagem se reflete no ano de 2022.")    
        dt = pd.read_csv('IPV_2022.csv', sep=';')
        fig = px.bar(data_frame=dt, x=dt['PONTO_VIRADA_2022'], y=dt['TOTAL'])
        st.plotly_chart(fig)

        st.write("")
        st.write("Estes resultados mostram que os alunos da instituição constantemente estão criando a conscientização da importância da educação em suas vidas.")
        st.write("Isso mostra que apesar de alguns resultados negativos em indicadores, o objetivo principal da instituição está sendo atingido.")
        st.write("Os alunos estão se tornando mais estudiosos, compartilham os conhecimentos obtidos, colaboram com o aprendizado dos colegas, melhoram se desenvolvimento emocional, criam o hábito de leitura, melhoram sua capacidade de raciocínio lógico, dentre outras grandes melhorias.")

    with st.expander("Indicador de Adequação de Nível - IAN"):
        st.title("Indicador de Adequação de Nível - IAN")
        st.write("Este indicador busca captar a condição da adequação do aluno em relação à Fase de Ensino a qual está designado.")
        st.write("O cálculo consiste em comparar a idade do aluno, e o ano escolar ideal a ser cursado dentro da estrutura do Ensino Médio e Fundamental.")
        st.write("Em seguida, estabelece qual a Fase de Ensino Ideal no Programa de Aceleração do Conhecimento, dado seu ano escolar ideal.")

        st.write("Dos alunos que participaram da Associação nos anos de 2020 à 2022, vemos que 71,65% aumentaram sua defasagem, enquanto 28,92% diminuiram")  
        dt = pd.read_csv('IAN_2020_2022.csv', sep=';')
        fig = px.bar(data_frame=dt, x=dt['TIPO'], y=dt['TOTAL'])
        st.plotly_chart(fig)

        st.write("")                
        st.write("Enquanto, os alunos que participaram nos anos de 2021 e 2022, 60,14% tiveram a defasagem aumentada.")
        dt = pd.read_csv('IAN_2021_2022.csv', sep=';')
        fig = px.bar(data_frame=dt, x=dt['TIPO'], y=dt['TOTAL'])
        st.plotly_chart(fig)

        st.write("")
        st.write("O mesmo ocorre com os alunos que participaram somente nos anos de 2020 e 2021, onde 75,52% aumentaram a defasagem.")    
        dt = pd.read_csv('IAN_2020_2021.csv', sep=';')
        fig = px.bar(data_frame=dt, x=dt['TIPO'], y=dt['TOTAL'])
        st.plotly_chart(fig)

        st.write("")
        st.write("Este resultado nos mostra uma oportunidade na Associação Passos Mágicos. Uma vez que há o aumento da defasagem, há necessidade de revermos alguma metodologia ou concentrarmos melhor em alguma necessidade individual dos alunos.")