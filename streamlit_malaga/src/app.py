from PIL import Image
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(layout="wide")

st.header("MalagaHouse")
st.text("Trabajo Fin de Máster FP en IA y Big Data realizado por \n Miguel Gámez Ruiz y Sergio Toscano Díaz")

tipo = st.selectbox('Introduzca el tipo de casa', ['Piso', 'Ático', 'Dúplex', 'Casa', 'Chalet', 'Finca rútica', 'Estudio', 'Loft'])
zona = st.selectbox('Introduzca el tipo de casa', ['Bailén-Miraflores', 'Centro', 'Este', 'Ciudad Jardín', 'Carretera de Cádiz', 'Teatinos-Universidad', 'La Rosaleda-La Roca', 'Cruz de Humilladero', 'Campanillas', 'Puerto de la Torre'])
superficie = st.slider('Introduzca la superficie', 1,1000)
habitaciones = st.number_input('Introduzca las habitaciones', 1,15)
banios = st.number_input('Introduzca los baños', 1,15)
garaje = st.selectbox('¿Tiene garaje?', ['Sí','No'])
trastero = st.selectbox('¿Tiene trastero?', ['Sí','No'])
ascensor = st.selectbox('¿Tiene ascensor?', ['Sí','No'])
terraza = st.selectbox('¿Tiene terraza?', ['Sí','No'])
amueblado = st.selectbox('¿Tiene amueblado?', ['Sí','No'])
chimenea = st.selectbox('¿Tiene chimenea?', ['Sí','No'])
piscina = st.selectbox('¿Tiene piscina?', ['Sí','No'])
jardin = st.selectbox('¿Tiene jardín?', ['Sí','No'])