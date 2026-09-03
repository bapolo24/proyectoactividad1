import streamlit as st


st.set_page_config(
    page_title="Oil & Gas Engineering",
    page_icon="🛢️",
    layout="wide",
    initial_sidebar_state="expanded"
)


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


paginas = [
    inicio,
    ejercicios
]


pagina = st.navigation(
    paginas
)


pagina.run()
