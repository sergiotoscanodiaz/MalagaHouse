# Import necessary libraries
from PIL import Image
import streamlit as st
import pandas as pd
import joblib
import time

# Set page configuration to wide layout
st.set_page_config(layout="wide")

# Load image and display it 
image = Image.open('malaga.jpg')
st.image(image, width = 600)

# Set header and subheader
st.header("MalagaHouse")
st.text("Trabajo Fin de Máster FP en IA y Big Data realizado por Miguel Gámez Ruiz y Sergio Toscano Díaz")

# Create three columns for user inputs
col1, col2, col3 = st.columns(3)
# Column 1: selectbox for type of house, selectbox for zone, and number inputs for bedrooms and bathrooms
with col1:
    category = st.selectbox('Introduzca el tipo de casa', ['Piso', 'Ático', 'Dúplex', 'Casa', 'Chalet', 'Finca rútica', 'Estudio', 'Loft'])
    zone = st.selectbox('Introduzca el tipo de casa', ['Bailén-Miraflores', 'Centro', 'Este', 'Ciudad Jardín', 'Carretera de Cádiz', 'Teatinos-Universidad', 'La Rosaleda-La Roca', 'Cruz de Humilladero', 'Campanillas', 'Puerto de la Torre'])
    room = st.number_input('Introduzca las habitaciones', 1,15)
    bath = st.number_input('Introduzca los baños', 1,15)
# Column 2: selectboxes for garage, storage, lift and terrace
with col2:
    garage = st.selectbox('¿Tiene garaje?', ['Sí','No'])
    storage = st.selectbox('¿Tiene trastero?', ['Sí','No'])
    lift = st.selectbox('¿Tiene ascensor?', ['Sí','No'])
    terrace = st.selectbox('¿Tiene terraza?', ['Sí','No'])
# Column 3: selectboxes for furniture, chimney, pool and garden
with col3:
    furniture = st.selectbox('¿Tiene amueblado?', ['Sí','No'])
    chimney = st.selectbox('¿Tiene chimenea?', ['Sí','No'])
    pool = st.selectbox('¿Tiene piscina?', ['Sí','No'])
    garden = st.selectbox('¿Tiene jardín?', ['Sí','No'])

# Slider for surface area input
surface = st.slider('Introduzca la superficie', 1,1000)

# If button is clicked, predict the price using the saved model
if st.button("¿Cuánto costará?", key="main_button"): 

    # Displays a message while executing the code
    with st.spinner('Espera un momento...'):
        time.sleep(2)

    # Load the saved model
    houses_model = joblib.load("houses_model.pkl")    
    # Create a dataframe with user inputs
    X = pd.DataFrame([[category, zone, surface, room, bath, garage, storage, lift, terrace, furniture, chimney, pool, garden]],
                     columns = ["Tipo","Zona","Superficie","Habitaciones","Baños","Garaje","Trastero","Ascensor","Terraza","Amueblado","Chimenea","Piscina","Jardín"])
    # Replace categorical variables with numerical values
    X = X.replace(['Bailén-Miraflores', 'Centro', 'Este', 'Ciudad Jardín', 'Carretera de Cádiz', 'Teatinos-Universidad', 'Churriana', 'La Rosaleda-La Roca', 'Cruz de Humilladero', 'Campanillas', 'Puerto de la Torre'],[0,1,2,3,4,5,6,7,8,9,10])
    X = X.replace(['Piso', 'Ático', 'Dúplex', 'Casa', 'Chalet', 'Finca rútica', 'Estudio', 'Loft'],[0,1,2,3,4,5,6,7])
    X = X.replace(["Sí", "No"], [1, 0])
    # Generates a prediction for the price of the house and display it. 
    prediction = houses_model.predict(X)[0]
    st.text(f"Esta vivienda se estima que costará {prediction} €")
