import streamlit as st

from estilos import cargar_estilos

from produccion import show as show_produccion
from perforacion import show as show_perforacion
from reservorios import show as show_reservorios


# ==========================================================
# CARGAR ESTILOS
# ==========================================================

cargar_estilos()


# ==========================================================
# ENCABEZADO
# ==========================================================

st.title(
    "📊 Ejercicios de Ingeniería de Petróleo"
)

st.write(
    """
    Seleccione el módulo técnico mediante las pestañas
    disponibles.
    """
)


# ==========================================================
# CREACIÓN DE TABS
# ==========================================================

tab1, tab2, tab3 = st.tabs(
    [
        "🛢️ Producción",
        "🏗️ Perforación",
        "🪨 Reservorios"
    ]
)


# ==========================================================
# PRODUCCIÓN
# ==========================================================

with tab1:

    show_produccion()


# ==========================================================
# PERFORACIÓN
# ==========================================================

with tab2:

    show_perforacion()


# ==========================================================
# RESERVORIOS
# ==========================================================

with tab3:

    show_reservorios()
