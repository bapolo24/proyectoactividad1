import streamlit as st

from produccion import show as show_produccion
from perforacion import show as show_perforacion
from reservorios import show as show_reservorios

from estilos import cargar_estilos


cargar_estilos()


st.title(
    "📊 Ejercicios de Ingeniería de Petróleo"
)

st.write(
    "Seleccione el área técnica que desea analizar."
)


tab1, tab2, tab3 = st.tabs(
    [
        "🛢️ Producción",
        "🏗️ Perforación",
        "🪨 Reservorios"
    ]
)


with tab1:

    show_produccion()


with tab2:

    show_perforacion()


with tab3:

    show_reservorios()
