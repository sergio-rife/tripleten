import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Análisis de anuncios de coches")

car_data = pd.read_csv("vehicles_us.csv")

st.write("Vista previa del conjunto de datos:")
st.dataframe(car_data.head())

hist_button = st.button("Construir histograma")

if hist_button:
    st.write("Histograma de la columna odometer")
    fig = px.histogram(
        car_data,
        x="odometer",
        title="Distribución del Odómetro"
    )
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button("Construir gráfico de dispersión")

if scatter_button:
    st.write("Relación entre odómetro y precio")
    fig = px.scatter(
        car_data,
        x="odometer",
        y="price",
        title="Relación entre Odómetro y Precio"
    )
    st.plotly_chart(fig, use_container_width=True)