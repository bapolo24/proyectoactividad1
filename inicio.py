import streamlit as st  # Importa Streamlit para crear la página de inicio y conservar datos.
st.title("Tarea Evaluativa – Módulo 1")  # Muestra el encabezado de la aplicación integrada.
st.write("Selecciona una herramienta o comienza directamente con la calculadora.")  # Orienta al usuario sobre las opciones disponibles.
st.page_link("produccion.py", label="Abrir Modulo de Prouccion", icon="🛢️")  # Crea un enlace visible hacia la calculadora.
st.page_link("perforacion.py", label="Abrir Modulo de Perforacion", icon="🏗️")  # Crea un segundo enlace visible hacia el resumen.
st.page_link("reservorios.py", label="Abrir Modulo de reservorios", icon="🌍")  # Crea un segundo enlace visible hacia el resumen.
