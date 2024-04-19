import streamlit as st

def grafico_dona(year,col):
    col.image(f'Images/donut_platform_year_{year}.png',caption = f'Porcentajes de películas en cada plataforma en el año {year}')
    
def grafico_hist(year):
    st.image(f'Images/histogram_age_year_{year}.png',caption = f'Histograma de edades permitidas en el año {year}')

def resumen_general():
    st.image(f'Images/visualization.png',caption = f'Resumen general')