import streamlit as st


# ==========================================================
# CONFIGURACIÓN GENERAL
# ==========================================================

st.set_page_config(
    page_title="Oil & Gas Engineering",
    page_icon="🛢️",
    layout="wide"
)


# ==========================================================
# PÁGINAS PRINCIPALES
# ==========================================================

inicio = st.Page(
    "inicio.py",
    title="Home",
    icon="🏠",
    default=True
)

ejercicios = st.Page(
    "ejercicios.py",
    title="Ejercicios",
    icon="📊"
)


# ==========================================================
# NAVEGACIÓN
# ==========================================================

pagina = st.navigation(
    [
        inicio,
        ejercicios
    ]
)


pagina.run()
