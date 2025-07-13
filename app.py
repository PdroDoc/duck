import streamlit as st
import duckdb
import pandas as pd

# 1. Título impactante
st.title("📊 Painel Dinâmico de Processos: Planilha sem Excel, via DuckDB")

# Sidebar GLOBAL
with st.sidebar:
    st.image("https://avatars.githubusercontent.com/u/205710427?v=4", caption="Advogado que programa é unicórnio!",
             use_container_width=True)
    st.markdown("---")


    st.header("Pedro Potz")
    st.markdown("Advogado Programador")
    st.link_button(" Visite meu novo site", "http://pedrop.vercel.app")


# NOVO: Introdução impactante sobre DuckDB
st.markdown("""
### Esqueça o Excel. Prepare-se para o DuckDB.

Você está acostumado com planilhas? Ótimo. Mas o que você vê aqui não é uma "simples" planilha.
Este é um **Painel Dinâmico de Processos** construído com uma tecnologia incrivelmente poderosa e surpreendentemente fácil de usar, chamada **DuckDB**.

**Pense assim:**
* **Não é Excel:** Enquanto o Excel é excelente para dados menores e manipulação manual, o DuckDB é um **banco de dados analítico** que vive dentro do seu programa. Ele processa milhões de linhas de dados em segundos, diretamente no seu computador, sem a necessidade de servidores complexos.
* **Seus dados, seu controle:** Carregamos dados de arquivos CSV e os consultamos com a velocidade e flexibilidade do SQL. Isso significa que você tem o poder de um banco de dados robusto, mas com a simplicidade de um arquivo que você já conhece.
* **Velocidade e Eficiência:** Para advogados que precisam analisar grandes volumes de processos, prazos e valores, o DuckDB permite análises complexas em um piscar de olhos, sem travar sua máquina ou exigir softwares caros.

**Curioso para ver como tudo isso funciona sem ser uma "planilha" comum?** Continue navegando!
""")

# 2. Texto introdutório (st.markdown) - Ajustado para complementar a nova intro
st.markdown("""
Este painel carrega dados de processos e calcula honorários diretamente de arquivos CSV,
usando SQL rápido com DuckDB. Uma ferramenta para advogados
que programam e buscam eficiência!
""")
st.markdown("Aqui usamos duas planilhas completamente independentes, e criamos uma consulta e vizualização a partir de ambas:")

# conectar ao DuckDB in-memory
con = duckdb.connect(database=':memory:')

# carregar dados (garantindo que os arquivos CSV estão no mesmo diretório ou forneça o caminho completo)
try:
    con.execute("""
        CREATE TABLE processos AS
        SELECT * FROM read_csv_auto('processos.csv')
    """)
    con.execute("""
        CREATE TABLE honorarios AS
        SELECT * FROM read_csv_auto('honorarios.csv')
    """)
except Exception as e:
    st.error(f"Erro ao carregar arquivos CSV. Certifique-se de que 'processos.csv' e 'honorarios.csv' estão no mesmo diretório do script. Detalhes: {e}")
    st.stop() # Parar a execução se os arquivos não forem encontrados

# Query principal para unir e calcular
query = """
    SELECT
        p.numero_processo,
        p.parte_contraria,
        p.valor_causa,
        p.prazo_final,
        p.status,
        h.honorario_percentual,
        ROUND(p.valor_causa * h.honorario_percentual / 100.0, 2) AS honorario_estimado
    FROM processos p
    JOIN honorarios h
    ON p.numero_processo = h.numero_processo
    ORDER BY p.prazo_final ASC
"""

df_join = con.execute(query).df()

# 3. Métricas resumidas (st.metric)
st.markdown("---")
col1, col2, col3 = st.columns(3)

total_processos = df_join.shape[0]
total_honorarios_estimados = df_join['honorario_estimado'].sum()
processos_em_andamento = df_join[df_join['status'].str.contains('Em Andamento', case=False, na=False)].shape[0]
processos_concluidos = df_join[df_join['status'].str.contains('Concluído', case=False, na=False)].shape[0]

with col1:
    st.metric(label="Total de Processos", value=total_processos)
with col2:
    st.metric(label="Total de Honorários Estimados", value=f"R$ {total_honorarios_estimados:,.2f}")
with col3:
    st.metric(label="Processos Em Andamento", value=processos_em_andamento)
    st.metric(label="Processos Concluídos", value=processos_concluidos) # Adicionado para completar a métrica

st.markdown("---")

# 4. Filtro interativo (st.selectbox)
status_options = ['Todos'] + list(df_join['status'].unique())
selected_status = st.selectbox("Filtrar por Status do Processo", status_options)

if selected_status != 'Todos':
    df_filtered = df_join[df_join['status'] == selected_status]
else:
    df_filtered = df_join

# 5. Gráfico (plotly)
st.subheader("Visualização de Valores por Processo")
if not df_filtered.empty:
    import plotly.express as px
    fig = px.bar(df_filtered,
                 x='numero_processo',
                 y=['valor_causa', 'honorario_estimado'],
                 barmode='group',
                 title='Valores de Causa e Honorários Estimados por Processo',
                 labels={'value': 'Valor (R$)', 'variable': 'Tipo de Valor'},
                 hover_data={'parte_contraria': True, 'status': True})
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("Nenhum dado para exibir com o filtro selecionado.")


# 6. Tabela final (st.dataframe) com destaque
st.subheader("Detalhes dos Processos")
if not df_filtered.empty:
    st.dataframe(df_filtered.style.highlight_max(axis=0, subset=['valor_causa', 'honorario_estimado'], color="lightgreen"))
else:
    st.info("Nenhum processo corresponde ao filtro selecionado.")

# 7. Rodapé (st.caption)
st.caption("Tecnologia: Python + DuckDB + Streamlit — ")

# Finaliza a conexão com o DuckDB
con.close()


st.markdown("---")



st.markdown("### Não perca  meus tutoriais e outras ferrramentas gratuitas.")
st.write("Estou aqui para guiá-los nessa jornada. Juntos, vamos desmistificar a tecnologia")
st.link_button("Conheça Mais" , "https://pedrop.vercel.app/", help="Aprenda a programar do zero ao avançado!")




st.markdown("---")
st.link_button("Geo -visualização Avançada", "https://runmapy.streamlit.app/")
st.link_button("Visualização de dados simples","https://sleepdataview.streamlit.app/")
st.link_button("Calculadoras Jurídicas avançada","")
st.markdown("---")

st.markdown("---")
st.markdown("""
        <div style='text-align: center; color: #666; font-size: 12px;'>
        Uma ferramenta desenvolvida por Pedro Potz<br>
        Advogado especializado em soluções jurídico-tecnológicas<br>
        🦄 <em>Advogado que programa é unicórnio!</em>
        </div>
        """, unsafe_allow_html=True)

