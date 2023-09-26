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
import math

# Entrada de valores
phi = float(input("Ingrese el valor de φ en grados: "))
delta = float(input("Ingrese el valor de δ en grados: "))
omega = float(input("Ingrese el valor de 𝜔 en grados: "))
d = float(input("Ingrese el valor de 𝑑: "))
dd = float(input("Ingrese el valor de đ: "))

# Convertir ángulos de grados a radianes
phi_rad = math.radians(phi)
delta_rad = math.radians(delta)
omega_rad = math.radians(omega)

# Calcular el valor de RA utilizando la fórmula
RA = 889 * (dd / d) * (0.01745 * omega_rad * math.sin(phi_rad) * math.sin(delta_rad) + math.cos(phi_rad) * math.cos(delta_rad) * math.sin(omega_rad))

# Imprimir el resultado
print(f"El valor de RA es: {RA}")

