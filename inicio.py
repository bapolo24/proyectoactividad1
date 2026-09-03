import streamlit as st
import textwrap

from estilos import cargar_estilos
from componentes import bloque_informativo
from interacciones import componente_javascript


# ==========================================================
# CARGAR ESTILOS
# ==========================================================

cargar_estilos()


# ==========================================================
# ENCABEZADO PRINCIPAL
# ==========================================================

st.title(
    "🛢️ Tarea Evaluativa – Módulo 1"
)


st.markdown(
    """
    ### Desarrollo de una aplicación web para Oil & Gas
    ### con Streamlit, HTML, CSS y JavaScript
    """
)


st.markdown(
    """
    **BOOTCAMP DATA ANALYTICS FOR OIL & GAS**
    """
)


st.divider()


# ==========================================================
# DESCRIPCIÓN GENERAL
# ==========================================================

bloque_informativo(

    "Descripción del proyecto",

    """
    Aplicación web interactiva orientada a Ingeniería de Petróleo.
    Integra tres ejercicios técnicos correspondientes a las áreas
    de Producción, Perforación y Reservorios, combinando cálculos
    de ingeniería con herramientas de visualización y desarrollo
    web mediante Streamlit, HTML, CSS y JavaScript.
    """,

    "🎯"
)


# ==========================================================
# MÓDULOS
# ==========================================================

st.subheader(
    "⚙️ Módulos Técnicos"
)


col1, col2, col3 = st.columns(3)


# ==========================================================
# PRODUCCIÓN
# ==========================================================

with col1:

    tarjeta_produccion = """
<div class="home-card">

    <div class="home-card-icon">
        🛢️
    </div>

    <div class="home-card-title">
        Producción
    </div>

    <div class="home-card-text">
        Análisis de desempeño de afluencia mediante
        una IPR compuesta para un reservorio inicialmente
        subsaturado.
        <br><br>
        <b>Modelo:</b><br>
        Lineal + Vogel
    </div>

</div>
"""

    st.markdown(
        textwrap.dedent(
            tarjeta_produccion
        ),
        unsafe_allow_html=True
    )


# ==========================================================
# PERFORACIÓN
# ==========================================================

with col2:

    tarjeta_perforacion = """
<div class="home-card">

    <div class="home-card-icon">
        🏗️
    </div>

    <div class="home-card-title">
        Perforación
    </div>

    <div class="home-card-text">
        Cálculo del gradiente y presión hidrostática
        generada por la columna de lodo de perforación.
        <br><br>
        <b>Análisis:</b><br>
        Sobrebalance / Balance / Bajo balance
    </div>

</div>
"""

    st.markdown(
        textwrap.dedent(
            tarjeta_perforacion
        ),
        unsafe_allow_html=True
    )


# ==========================================================
# RESERVORIOS
# ==========================================================

with col3:

    tarjeta_reservorios = """
<div class="home-card">

    <div class="home-card-icon">
        🪨
    </div>

    <div class="home-card-title">
        Reservorios
    </div>

    <div class="home-card-text">
        Estimación volumétrica del Petróleo Original
        en Sitio y del volumen potencialmente recuperable.
        <br><br>
        <b>Modelo:</b><br>
        Método volumétrico del POES
    </div>

</div>
"""

    st.markdown(
        textwrap.dedent(
            tarjeta_reservorios
        ),
        unsafe_allow_html=True
    )


# ==========================================================
# INSTRUCCIÓN DE NAVEGACIÓN
# ==========================================================

st.write("")


st.info(
    "📊 Seleccione **Ejercicios** en el menú lateral para "
    "acceder a los cálculos de Producción, Perforación "
    "y Reservorios."
)


# ==========================================================
# COMPONENTE JAVASCRIPT
# ==========================================================

st.subheader(
    "💻 Interacción Web"
)


st.write(
    "El siguiente componente incorpora una interacción "
    "implementada mediante JavaScript."
)


componente_javascript()
