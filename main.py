import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_csv('supermarket_sales.csv', sep=';', decimal=',')

# Alterei o tipo da coluna data e ordenei o df por ela
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(by='Date')

# Criei uma nova coluna onde será somente o mes e ano do 'Date' e criei um sidebar onde ocorre um selected
df['Month'] = df['Date'].apply(lambda x: str(x.year) + '-' + str(x.month))
month = st.sidebar.selectbox("Mês", df['Month'].unique())

# Filtro para mostrar o data frame perante o mes selecionado
df_filtered = df[df['Month'] == month]
df_filtered

# Criação das colunas
col1, col2 = st.columns(2)
col3, col4, col5 = st.collums(3)