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

st.markdown(
    """
    <div style="
        text-align: center;
        padding-top: 10px;
        padding-bottom: 10px;
    ">

        <h1 style="
            color: #1F2937;
            margin-bottom: 10px;
        ">
            🛢️ Tarea Evaluativa – Módulo 1
        </h1>


        <h3 style="
            color: #374151;
            font-weight: 600;
            margin-bottom: 10px;
        ">
            Desarrollo de una aplicación web para Oil & Gas
            con Streamlit, HTML, CSS y JavaScript
        </h3>


        <p style="
            color: #4B5563;
            font-size: 18px;
            font-weight: bold;
        ">
            BOOTCAMP DATA ANALYTICS FOR OIL & GAS
        </p>

    </div>
    """,

    unsafe_allow_html=True
)


st.divider()


# ==========================================================
# DESCRIPCIÓN DEL PROYECTO
# ==========================================================

bloque_informativo(

    "Objetivo del Proyecto",

    """
    Desarrollar una aplicación web interactiva orientada
    a la Ingeniería de Petróleo, integrando cálculos
    técnicos de Producción, Perforación y Reservorios
    mediante Python y Streamlit.

    La aplicación incorpora además elementos personalizados
    mediante HTML, CSS, JavaScript y visualizaciones
    interactivas con Plotly.
    """,

    "🎯"
)


# ==========================================================
# MÓDULOS TÉCNICOS
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
        PRODUCCIÓN
    </div>

    <div class="home-card-text">

        Análisis del desempeño de afluencia
        mediante una IPR compuesta.

        <br><br>

        <b>Modelo técnico</b>

        <br>

        Región Lineal + Vogel

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
        PERFORACIÓN
    </div>

    <div class="home-card-text">

        Cálculo del gradiente y
        presión hidrostática del
        fluido de perforación.

        <br><br>

        <b>Análisis técnico</b>

        <br>

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
        RESERVORIOS
    </div>

    <div class="home-card-text">

        Estimación volumétrica del
        Petróleo Original en Sitio.

        <br><br>

        <b>Modelo técnico</b>

        <br>

        POES + Volumen Recuperable

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
    "📊 Seleccione **Ejercicios** en el menú lateral "
    "para acceder a los módulos de Producción, "
    "Perforación y Reservorios."
)


# ==========================================================
# TECNOLOGÍAS UTILIZADAS
# ==========================================================

st.subheader(
    "💻 Tecnologías Utilizadas"
)


col4, col5, col6, col7 = st.columns(4)


with col4:

    st.markdown(
        """
        <div class="home-card">

            <div class="home-card-icon">
                🐍
            </div>

            <div class="home-card-title">
                Python
            </div>

            <div class="home-card-text">
                Lógica y cálculos
                de ingeniería
            </div>

        </div>
        """,

        unsafe_allow_html=True
    )


with col5:

    st.markdown(
        """
        <div class="home-card">

            <div class="home-card-icon">
                🎈
            </div>

            <div class="home-card-title">
                Streamlit
            </div>

            <div class="home-card-text">
                Desarrollo de la
                aplicación web
            </div>

        </div>
        """,

        unsafe_allow_html=True
    )


with col6:

    st.markdown(
        """
        <div class="home-card">

            <div class="home-card-icon">
                🎨
            </div>

            <div class="home-card-title">
                HTML + CSS
            </div>

            <div class="home-card-text">
                Diseño y tarjetas
                personalizadas
            </div>

        </div>
        """,

        unsafe_allow_html=True
    )


with col7:

    st.markdown(
        """
        <div class="home-card">

            <div class="home-card-icon">
                ⚡
            </div>

            <div class="home-card-title">
                JavaScript
            </div>

            <div class="home-card-text">
                Interacciones
                dinámicas
            </div>

        </div>
        """,

        unsafe_allow_html=True
    )


# ==========================================================
# INTERACCIÓN JAVASCRIPT
# ==========================================================

st.subheader(
    "⚡ Componente Interactivo con JavaScript"
)


st.write(
    "Este componente demuestra una interacción visible "
    "implementada mediante JavaScript, de acuerdo con "
    "los requisitos de la actividad."
)


componente_javascript()


# ==========================================================
# PIE DE PÁGINA
# ==========================================================

st.divider()


st.markdown(
    """
    <div style="
        text-align: center;
        color: #4B5563;
        padding-bottom: 20px;
    ">

        <b>
            BOOTCAMP DATA ANALYTICS FOR OIL & GAS
        </b>

        <br>

        Aplicación desarrollada con
        Python + Streamlit

    </div>
    """,

    unsafe_allow_html=True
)
