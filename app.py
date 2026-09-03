import streamlit as st


# ==========================================================
# CONFIGURACIÓN GENERAL DE LA APLICACIÓN
# ==========================================================

st.set_page_config(
    page_title="Oil & Gas Engineering",
    page_icon="🛢️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================================
# DEFINICIÓN DE PÁGINAS
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
# NAVEGACIÓN PRINCIPAL
# ==========================================================

paginas = [
    inicio,
    ejercicios
]

pagina = st.navigation(
    paginas
)


# ==========================================================
# EJECUTAR PÁGINA
# ==========================================================

pagina.run()
