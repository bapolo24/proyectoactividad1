import streamlit as st  # Importa Streamlit para crear la página de inicio y conservar datos.
st.title("Aplicación multipágina")  # Muestra el encabezado de la aplicación integrada.
if "sg" not in st.session_state: st.session_state.sg = 0.85  # Inicializa la gravedad específica una sola vez por sesión.
st.write("Selecciona una herramienta o comienza directamente con la calculadora.")  # Orienta al usuario sobre las opciones disponibles.
st.page_link("api.py", label="Abrir Calculadora API", icon="🛢️")  # Crea un enlace visible hacia la calculadora.
st.page_link("resumen.py", label="Ver Resumen", icon="📊")  # Crea un segundo enlace visible hacia el resumen.
