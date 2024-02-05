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
col3, col4, col5 = st.columns(3)

# Faturamento por mes 
fat_date = px.bar(df_filtered, x='Date', y='Total', color='City', title='Faturamento por mês')
col1.plotly_chart(fat_date)
# Produtos mais vendidos por tempo
prod_date = px.bar(df_filtered, x='Date', y='Product line', color='City', title='Faturamento por tipo de produto', orientation='h')
col2.plotly_chart(prod_date)
#Faturamento por filial
city_total = df_filtered.groupby('City')[['Total']].sum().reset_index()
city_date = px.bar(city_total, x='City', y='Total', title='Faturamento por filial')
col3.plotly_chart(city_date)