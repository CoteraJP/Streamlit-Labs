import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

walmart_link ='https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv'
walmart_data = pd.read_csv(walmart_link)

st.title('TEMA 2: Interacción con otros componentes - Visualización de analítica de datos para WalMart USA')

st.write("""Visualización de analítica de 
datos para WalMart USA con la predicción 
de ventas de productos de línea blanca en el noroeste de USA.""")

sidebar = st.sidebar
sidebar.title("Visualización - WalMart USA")
sidebar.write("Opciones:")

selected_shipmod = sidebar.radio("Modo de Distribución:", walmart_data['Ship Mode'].unique())

st.success(f"Modo de Distribución: {selected_shipmod}")
st.markdown("___")

selected_cat = sidebar.selectbox("Seleccionar Categoría", walmart_data['Category'].unique())

st.success(f"Categoría seleccionada: {selected_cat}")
st.markdown("___")

# Slider Descuento
disc_select = sidebar.slider(
"Seleccionar el Descuento",
min_value=float(walmart_data['Discount'].min()),
max_value=float(walmart_data['Discount'].max())
)

st.markdown("___")

#Filtro Dataframe
wal_filt=walmart_data.loc[(walmart_data['Discount'] == disc_select) & 
(walmart_data['Ship Mode'] == selected_shipmod) & 
(walmart_data['Category'] == selected_cat)]

st.dataframe(wal_filt)    