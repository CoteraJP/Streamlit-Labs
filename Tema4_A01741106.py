import streamlit as st
import numpy as np
import pandas as pd
import datetime

DATA_URL = 'uber-raw-data-sep14.csv'
DATE_COLUMN = 'Date/Time'

st.title('TEMA 4: Visualización de Mapas - Viajes de Uber en NY')

st.write("""Visualización de  en un 
mapa de la ciudad de Nueva York los viajes realizados 
por la empresa Uber con filtros por hora""")

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    data.rename(lowercase, axis='columns', inplace = True)
    return data

data = load_data(1000)
st.dataframe(data)

st.map(data)

st.markdown("___")

hour_select = st.slider(
"Selecciona la hora",
min_value=int(0),
max_value=int(23)
)

filtered_data = data[data['date/time'].dt.hour == hour_select]

st.write(f"Número de viajes a las {hour_select} horas: {filtered_data.shape[0]}")
st.dataframe(filtered_data)
st.map(filtered_data)