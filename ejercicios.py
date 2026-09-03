import streamlit as st

from produccion import show as show_produccion
from perforacion import show as show_perforacion
from reservorios import show as show_reservorios

from estilos import cargar_estilos


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
    "Seleccione el área técnica que desea analizar."
)


# ==========================================================
# TABS DE LOS EJERCICIOS
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
