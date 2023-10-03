import streamlit as st
import pandas as pd
import math
#dias año
dn = pd.read_csv("https://raw.githubusercontent.com/Frank10OC/Radiacion/main/DIAS.csv")
st.write("Dias del año")
st.dataframe(dn)
# Quitar la primera y segunda fila
df = dn.iloc[2:]
# Quitar la primera columna
df = dn.iloc[:, 1:]
st.dataframe(df)
# Función para calcular la radiación solar
def calcular_radiacion_solar(N):
    Ics = 4921.2  # Radiación solar extraterrestre en W/m^2
    angulo_solar = 360 * N / 365
    coseno_term = 0.0033 * math.cos(math.radians(angulo_solar))
    radiacion_solar = Ics * (1 + coseno_term)
    return radiacion_solar


# Agregar una columna 'RadiacionSolar' para almacenar los resultados
operaciones = dn.apply(calcular_radiacion_solar)

# Configurar la aplicación Streamlit
st.title('Operaciones con DataFrame')
st.sidebar.header('Configuración')

# Mostrar el DataFrame 'operaciones' en la interfaz
st.write(operaciones)

# Opcional: Guardar el DataFrame 'operaciones' en un archivo CSV
if st.button('Guardar DataFrame'):
    operaciones.to_csv('operaciones_radiacion_solar.csv', index=False)
    st.success('DataFrame guardado en operaciones_radiacion_solar.csv')





####
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

# Función para calcular d
dd=1.4968*pow(10,13) #cm đ
def calcular_d(n, dd):
    d = dd * (1 + 0.17 * math.sin(grados_a_radianes(0.9856 * n)))
    return d

# Botón para realizar el cálculo
if st.button("Calcular d"):
    resultado = calcular_d(n, dd)
    st.write(f"El valor de d es: {resultado}")
    x=pow(dd/resultado,2)
    st.write(f"El valor de d es:",x)
import streamlit as st
import math

# Título de la aplicación
st.title("Cálculo de Cos(𝜔o)")

# Entrada de valores
phi = st.number_input("Ingrese el valor de ϕ en grados:")
delta = st.number_input("Ingrese el valor de δ en grados:")

# Función para calcular Cos(𝜔o)
def calcular_cos_omega(phi, delta):
    # Convertir ángulos de grados a radianes
    phi_rad = math.radians(phi)
    delta_rad = math.radians(delta)
    
    # Calcular Cos(𝜔o)
    cos_omega = -math.tan(phi_rad) * math.tan(delta_rad)
    return cos_omega

# Botón para realizar el cálculo
if st.button("Calcular Cos(𝜔o)"):
    resultado = calcular_cos_omega(phi, delta)
    resultado =math.degrees(math.acos(resultado))
    st.write(f"El valor de 𝜔o es: {resultado:.4f}")

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
