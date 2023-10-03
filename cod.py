import streamlit as st
import math

# Título de la aplicación
st.title("Radiación Solar en la Atmósfera Exterior")

# Entradas para latitud, ángulo horario y declinación solar
latitud = st.number_input("Latitud (en grados):", min_value=-90, max_value=90, value=0)
angulo_horario = st.number_input("Ángulo Horario (en grados):", min_value=0, max_value=360, value=0)
declinacion_solar = st.number_input("Declinación Solar (en grados):", min_value=-90, max_value=90, value=0)

# Cálculo de la radiación solar
def calcular_radiacion_solar(latitud, angulo_horario, declinacion_solar):
    Io = 1361  # Intensidad solar promedio en W/m^2
    phi = math.radians(latitud)
    delta = math.radians(declinacion_solar)
    omega_s = math.radians(angulo_horario)

    Ho = (24 / math.pi) * Io * ((math.pi / 180) * omega_s * math.sin(delta) * math.sin(phi) + math.cos(delta) * math.cos(phi) * math.sin(omega_s))
    return Ho

if st.button("Calcular Radiación Solar"):
    radiacion_solar = calcular_radiacion_solar(latitud, angulo_horario, declinacion_solar)
    st.write(f"La radiación solar en la atmósfera exterior es de {radiacion_solar:.2f} W/m^2")

