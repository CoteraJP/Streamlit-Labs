import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

walmart_link ='https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv'
walmart_data = pd.read_csv(walmart_link)

st.title('TEMA 3: Gráficas en Streamlit - Visualización de analítica de datos para WalMart USA')

st.write("""Visualización de analítica de 
datos para WalMart USA con la predicción 
de ventas de productos de línea blanca en el noroeste de USA.""")

#Histograma con regiones
fig, ax = plt.subplots()
st.header("Histograma de Ventas por Región")

selected_reg = st.selectbox("Seleccionar Región", walmart_data['Region'].unique())
st.success(f"Región seleccionada: {selected_reg}")
wal_filt2=walmart_data.loc[(walmart_data['Region'] == selected_reg)]

ax.hist(wal_filt2.Sales)
st.pyplot(fig)

#Histograma por categorías
fig1_1, ax1_1 = plt.subplots()

st.header("Histograma de Cantidades Vendidas por Categoría")

selected_cat = st.selectbox("Seleccionar Categoría", walmart_data['Category'].unique())
st.success(f"Categoría seleccionada: {selected_cat}")
wal_filt=walmart_data.loc[(walmart_data['Category'] == selected_cat)]

ax1_1.hist(wal_filt.Quantity)
st.pyplot(fig1_1)
st.markdown("___")

#Barras
fig2, ax2 = plt.subplots()
y_pos = walmart_data['Sales']
x_pos = walmart_data['Region']
ax2.bar(x_pos, y_pos)
ax2.set_ylabel("Ventas")
ax2.set_xlabel("Región")
ax2.set_title('Ventas por Región')
st.header("Grafica de Barras - Ventas por Región")
st.pyplot(fig2)
st.markdown("___")

#PieCharts
fig3, ax3 = plt.subplots()
coupdovent = walmart_data.groupby('Category').sum()
leibol = list(pd.unique(walmart_data['Category']))
ax3.pie(coupdovent.Sales, labels=leibol, autopct='%.2f%%')
st.header("Grafica de Pastel - Ventas por Categoría")
st.pyplot(fig3)

fig4, ax4 = plt.subplots()
#coupdovent = walmart_data.groupby('Category').sum()
#leibol = list(pd.unique(walmart_data['Category']))
ax4.pie(coupdovent.Profit, labels=leibol, autopct='%.2f%%')
st.header("Grafica de Pastel - Ganancias por Categoría")
st.pyplot(fig4)