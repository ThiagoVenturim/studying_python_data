#importando as bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px

# ----- Configurações da página -----
st.set_page_config(
    page_title="Dashboard - Análise de Salário na Área de Dados",
    page_icon="📊",
    layout="wide"
)

# ----- Carregando dados -----
df = pd.read_csv(
    "https://raw.githubusercontent.com/ThiagoVenturim/studying_python_data/main/Alura/salarios_limpo.csv"
)

# ----- Barra Lateral -----
st.sidebar.header("Filtros")

# Filtro de Ano de Trabalho
ano_de_trabalho_disponiveis = sorted(df['ano_de_trabalho'].unique())
ano_de_trabalho_selecionado = st.sidebar.multiselect(
    "Ano de Trabalho",
    ano_de_trabalho_disponiveis,
    default=ano_de_trabalho_disponiveis
)

# Filtro de Senioridade
senioridade_disponiveis = sorted(df['nível_de_experiência'].unique())
nivel_senioridade_selecionado = st.sidebar.multiselect(
    "Nível de Experiência",
    senioridade_disponiveis,
    default=senioridade_disponiveis
)

# Filtro de Tamanho da Empresa
tamanho_empresa_disponiveis = sorted(df['porte_da_empresa'].unique())
tamanho_empresa_selecionado = st.sidebar.multiselect(
    "Porte da Empresa",
    tamanho_empresa_disponiveis,
    default=tamanho_empresa_disponiveis
)

# Filtro por Tipo de Contratação
tipo_contratacao_disponiveis = sorted(df['tipo_de_emprego'].unique())
tipo_contratacao_selecionado = st.sidebar.multiselect(
    "Tipo de Contratação",
    tipo_contratacao_disponiveis,
    default=tipo_contratacao_disponiveis
)

# ----- Filtragem do DataFrame -----
df_filtrado = df[
    (df['ano_de_trabalho'].isin(ano_de_trabalho_selecionado)) &
    (df['nível_de_experiência'].isin(nivel_senioridade_selecionado)) &
    (df['porte_da_empresa'].isin(tamanho_empresa_selecionado)) &
    (df['tipo_de_emprego'].isin(tipo_contratacao_selecionado))
]

# ----- Conteúdo Principal -----
st.title("Dashboard de Análise de Salário na Área de Dados")
st.markdown(
    "Explore os dados salariais na área de dados nos últimos anos. "
    "Utilize os filtros à esquerda para refinar a análise."
)

# ----- Métricas Principais (KPIs) -----
st.subheader("Métricas Gerais (Salário anual em USD)")

if not df_filtrado.empty:
    salario_medio = df_filtrado["salário_em_usd"].mean()
    salario_maximo = df_filtrado["salário_em_usd"].max()
    total_registro = df_filtrado.shape[0]
    cargo_mais_frequente = df_filtrado["cargo_profissional"].mode()[0]
else:
    salario_medio, salario_maximo, total_registro, cargo_mais_frequente = 0, 0, 0, ""

col1, col2, col3, col4 = st.columns(4)
col1.metric("Salário Médio", f"${salario_medio:,.0f}")
col2.metric("Salário Máximo", f"${salario_maximo:,.0f}")
col3.metric("Total de Registros", f"{total_registro:,}")
col4.metric("Cargo Mais Frequente", cargo_mais_frequente)

st.markdown("---")

# ----- Análises Visuais com Plotly -----
st.subheader("Gráficos")

# Gráfico 1 - Top 10 cargos por salário médio
col_graf1, col_graf2 = st.columns(2)
with col_graf1:
    if not df_filtrado.empty:
        top_cargos = (
            df_filtrado.groupby('cargo_profissional')['salário_em_usd']
            .mean()
            .nlargest(10)
            .sort_values(ascending=True)
            .reset_index()
        )
        grafico_cargos = px.bar(
            top_cargos,
            x='salário_em_usd',
            y='cargo_profissional',
            orientation='h',
            title="Top 10 cargos por salário médio",
            labels={'salário_em_usd': 'Média salarial anual (USD)', 'cargo_profissional': ''}
        )
        grafico_cargos.update_layout(title_x=0.1, yaxis={'categoryorder': 'total ascending'})
        st.plotly_chart(grafico_cargos, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de cargos.")

# Gráfico 2 - Distribuição de salários
with col_graf2:
    if not df_filtrado.empty:
        grafico_hist = px.histogram(
            df_filtrado,
            x='salário_em_usd',
            nbins=30,
            title="Distribuição de salários anuais",
            labels={'salário_em_usd': 'Faixa salarial (USD)', 'count': ''}
        )
        grafico_hist.update_layout(title_x=0.1)
        st.plotly_chart(grafico_hist, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de distribuição.")

# Gráfico 3 - Proporção remota
col_graf3, col_graf4 = st.columns(2)
with col_graf3:
    if not df_filtrado.empty:
        remoto_contagem = df_filtrado['proporção_remota'].value_counts().reset_index()
        remoto_contagem.columns = ['proporção_remota', 'quantidade']
        grafico_remoto = px.pie(
            remoto_contagem,
            names='proporção_remota',
            values='quantidade',
            title='Proporção dos tipos de trabalho',
            hole=0.5
        )
        grafico_remoto.update_traces(textinfo='percent+label')
        grafico_remoto.update_layout(title_x=0.1)
        st.plotly_chart(grafico_remoto, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico dos tipos de trabalho.")

# Gráfico 4 - Salário médio de Cientistas de Dados por país
with col_graf4:
    if not df_filtrado.empty:
        df_ds = df_filtrado[df_filtrado['cargo_profissional'] == 'Data Scientist']
        if not df_ds.empty:
            media_ds_pais = df_ds.groupby('residência_do_funcionário')['salário_em_usd'].mean().reset_index()
            grafico_paises = px.choropleth(
                media_ds_pais,
                locations='residência_do_funcionário',
                locationmode='country names',
                color='salário_em_usd',
                color_continuous_scale='rdylgn',
                title='Salário médio de Cientista de Dados por país',
                labels={'salário_em_usd': 'Salário médio (USD)', 'residência_do_funcionário': 'País'}
            )
            grafico_paises.update_layout(title_x=0.1)
            st.plotly_chart(grafico_paises, use_container_width=True)
        else:
            st.warning("Nenhum dado de Cientista de Dados para exibir no gráfico de países.")
    else:
        st.warning("Nenhum dado para exibir no gráfico de países.")

# ----- Tabela de Dados Detalhados -----
st.subheader("Dados Detalhados")
st.dataframe(df_filtrado)
