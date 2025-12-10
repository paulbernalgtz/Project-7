import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Título de la app
st.title("Proyecto Sprint 7")
st.markdown("---")
st.header("Panel de control: Anuncios de Autos")

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')

# Checkbox para histograma
if st.checkbox("Mostrar/Ocultar Histograma"):
    # Escribir un mensaje en la aplicación
    st.header("Gráfico de Histograma")
    st.write('Histograma para el conjunto de datos de anuncios de venta de coches.')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'],
        marker_color="#16DA20",
        opacity=0.75
    )])
                                       
    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(
        title_text='Distribución del Odómetro',
        xaxis_title='Kilometraje',
        yaxis_title='N° de vehículos',
    )

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    st.plotly_chart(fig, use_container_width=True)

# Checkbox para gráfico de dispersión
if st.checkbox("Mostrar/Ocultar Gráfico de Dispersión"):
    st.header("Gráfico de Dispersión")
    st.write("Gráfico de Dispersión: Año y precio")
    fig_scatter = px.scatter(car_data, x='model_year', y='price', 
                             color='condition', hover_data=['model'],
                             color_discrete_sequence=px.colors.qualitative.Bold,
                             opacity=0.75,
                             labels={'model_year': 'Año del Vehículo', 'price': 'Precio (USD)'},
                             title="Precio vs Año del vehículo")
    st.plotly_chart(fig_scatter, use_container_width=True)
