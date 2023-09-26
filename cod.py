import streamlit as st

# Título de la aplicación
st.title("Aplicación de Saludo")

# Entrada del usuario
nombre = st.text_input("Por favor, ingresa tu nombre")

# Verificación si se ingresó un nombre
if nombre:
    # Salida personalizada
    st.write(f"Hola, {nombre}! Bienvenido a mi aplicación de Streamlit.")
else:
    st.write("Por favor, ingresa tu nombre en el cuadro de texto arriba.")
