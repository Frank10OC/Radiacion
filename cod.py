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
import streamlit as st
def grados_a_radianes(grados):
    radianes = math.radians(grados)
    return radianes

# Título de la aplicación
st.title("Cálculo de δ")

# Entrada de valores
n = st.number_input("Ingrese el valor de n:")

# Función para calcular δ
def calcular_delta(n):
    delta = 23.45 * math.sin(grados_a_radianes(0.9856 * n))
    return delta

# Botón para realizar el cálculo
if st.button("Calcular δ"):
    resultado = calcular_delta(n)
    st.write(f"El valor de δ es: {resultado}")

# Título de la aplicación
st.title("Cálculo de d")

# Entrada de valores
n = st.number_input("Ingrese el valor de n:")
dd = st.number_input("Ingrese el valor de đ:")

# Función para calcular d
def calcular_d(n, dd):
    d = dd * (1 + 0.17 * math.sin(0.9856 * n))
    return d

# Botón para realizar el cálculo
if st.button("Calcular d"):
    resultado = calcular_d(n, dd)
    st.write(f"El valor de d es: {resultado}")

# Título de la aplicación
st.title("Cálculo de δ")

# Entrada de valores
n = st.number_input("Ingrese el valor de n:")

# Función para calcular δ
def calcular_delta(n):
    delta = 23.45 * math.sin(0.9856 * n)
    return delta

# Botón para realizar el cálculo
if st.button("Calcular δ"):
    resultado = calcular_delta(n)
    st.write(f"El valor de δ es: {resultado}")

# Título de la aplicación
st.title("Cálculo de d")

# Entrada de valores
n = st.number_input("Ingrese el valor de n:")
dd = st.number_input("Ingrese el valor de đ:")

# Función para calcular d
def calcular_d(n, dd):
    d = dd * (1 + 0.17 * math.sin(0.9856 * n))
    return d

# Botón para realizar el cálculo
if st.button("Calcular d"):
    resultado = calcular_d(n, dd)
    st.write(f"El valor de d es: {resultado}")

# Título de la aplicación
st.title("Cálculo de RA")

# Entrada de valores
phi = st.number_input("Ingrese el valor de φ en grados:")
delta = st.number_input("Ingrese el valor de δ en grados:")
omega = st.number_input("Ingrese el valor de 𝜔 en grados:")
d = st.number_input("Ingrese el valor de 𝑑:")
dd = st.number_input("Ingrese el valor de đ:")

# Función para calcular RA
def calcular_ra(phi, delta, omega, d, dd):
    phi_rad = math.radians(phi)
    delta_rad = math.radians(delta)
    omega_rad = math.radians(omega)
    
    RA = 889 * pow((dd / d),2) * (0.01745 * omega_rad * math.sin(phi_rad) * math.sin(delta_rad) + math.cos(phi_rad) * math.cos(delta_rad) * math.sin(omega_rad))
    return RA
# Botón para realizar el cálculo
if st.button("Calcular RA"):
    resultado = calcular_ra(phi, delta, omega, d, dd)
    st.write(f"El valor de RA es: {resultado}")
