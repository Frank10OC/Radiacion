import streamlit as st
import math

# Título de la aplicación
st.title("Cálculo de Radiación Solar en la Atmósfera Exterior")

# Entradas para las variables
Io = st.number_input("Radiación solar extraterrestre (Io) [W/m^2]:", min_value=0.0, value=1361.0, step=1.0)
delta = st.number_input("Declinación solar (δ) [grados]:", min_value=-90.0, max_value=90.0, value=0.0, step=1.0)
phi = st.number_input("Latitud (ϕ) [grados]:", min_value=-90.0, max_value=90.0, value=0.0, step=1.0)
omega_s = st.number_input("Hora del día (ωs) [grados]:", min_value=0.0, max_value=360.0, value=0.0, step=1.0)

# Calcular la radiación solar
if st.button("Calcular"):
    try:
        # Convertir grados a radianes
        delta_rad = math.radians(delta)
        phi_rad = math.radians(phi)
        omega_s_rad = math.radians(omega_s)

        # Calcular la radiación solar
        Ho = (24 / math.pi) * Io * ((math.pi / 180) * omega_s_rad * math.sin(delta_rad) * math.sin(phi_rad) + math.cos(delta_rad) * math.cos(phi_rad) * math.sin(omega_s_rad))

        # Mostrar el resultado
        st.success(f"La radiación solar en la atmósfera exterior (Ho) es aproximadamente {Ho:.2f} W/m^2.")
    except Exception as e:
        st.error(f"Ocurrió un error en el cálculo: {e}")
