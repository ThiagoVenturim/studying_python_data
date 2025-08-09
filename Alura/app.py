#importando as bibliotecas
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px


#-----Configurações da página-----
#Definição do título da página, o icone e o layout pata ocupar a largura total
st.set_page_config(
    page_title="Dashboard - Análise de Salario Na Area de Dados",
    page_icon="📊",
    layout="wide"
)
df = pd.read_csv("https://github.com/ThiagoVenturim/studying_python_data/blob/main/Alura/salarios_limpo.csv") #lendo o arquivo csv


#-----Barra Lateral-----
st.sidebar.header("Filtros") #título da barra lateral

#Filtro de Ano de Trabalho
ano_de_trabalho_disponiveis = sorted(df['ano_de_trabalho'].unique()) #pegando os anos de trabalho disponíveis no dataframe
ano_de_trabalho_selecionado = st.sidebar.multiselect("Ano de Trabalho", ano_de_trabalho_disponiveis, default=ano_de_trabalho_disponiveis) #criando o filtro de anos

#Filtro Ano de Experiência
anos_disponiveis = sorted(df['ano_experiencia'].unique()) #pegando os anos disponíveis no dataframe
ano_selecionado = st.sidebar.multiselect("Ano de Experiência", anos_disponiveis, default=anos_disponiveis) #criando o filtro de anos

#Filtro de Senioridade
senioridade_disponiveis = sorted(df['nível_de_experiência'].unique()) #pegando os níveis de senioridade disponíveis no dataframe
nivel_senioridade_selecionado = st.sidebar.multiselect("nível_de_experiência"	, senioridade_disponiveis, default=senioridade_disponiveis) #criando o filtro de senioridade

#Filtro de Tamanho da Empresa
tamanho_empresa_disponiveis = sorted(df['porte_da_porte_da_empresa'].unique()) #pegando os tamanhos de empresa disponíveis no dataframe
tamanho_empresa_selecionado = st.sidebar.multiselect("Porte da Empresa", tamanho_empresa_disponiveis, default=tamanho_empresa_disponiveis) #criando o filtro de tamanho da empresa

#Filtro por Tipo de Contratação
tipo_contratacao_disponiveis = sorted(df['tipo_de_emprego'].unique()) #pegando os tipos de contratação disponíveis no dataframe
tipo_contratacao_selecionado = st.sidebar.multiselect("Tipo de Contratação", tipo_contratacao_disponiveis, default=tipo_contratacao_disponiveis) #criando o filtro de tipo de contratação

#Filtragem do DataFrame
df_filtrado = df[
    (df['ano_de_trabalho'].isin(ano_de_trabalho_selecionado)) &
    (df['nível_de_experiência'].isin(nivel_senioridade_selecionado)) &
    (df['porte_da_porte_da_empresa'].isin(tamanho_empresa_selecionado)) &
    (df['tipo_de_emprego'].isin(tipo_contratacao_selecionado))
]

#Conteudo Principal
st.title ("DashBord de Analise de Salario na Area de Dados")
st.markdown("Explore os dados salarias na area de dados nos Ultimos Anos, Utilize os filtros a esquerda para refinar os dados")


# Metricas Principais (KPIs)
st.subheader("Metricas getais (Salário anual em USD)")

if not df_filtrado:
    salario_medio = df_filtrado["salário_em_usd"].mean
    salario_maximo= df_filtrado["salário_em_usd"].max
    total_registro = df_filtrado.shape(0)
    cargo_mais_frequente = df_filtrado["cargo_profissional"].mode()[0]
else:
    salario_medio, salario_maximo, total_registro, salario_mediano, cargo_mais_comun = 0, 0, 0, ""

col1, col2, col3, col4 = st.columns(4)
col1.metric("Salario Medio", f"${salario_medio:,.0f}")
col2.metric("Salario Maximo",f"${salario_maximo:,.0f}")
col3.metric("Total de Registros", f"{total_registro:,}")
col4.metric("Cargo Mais Frequente ", cargo_mais_frequente)

st.markdown("---")
