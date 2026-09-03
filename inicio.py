import streamlit as st

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
### Desarrollo de una aplicación web para Oil & Gas con Streamlit, HTML, CSS y JavaScript
"""
)


st.markdown(
    """
### 🎓 BOOTCAMP DATA ANALYTICS FOR OIL & GAS
"""
)


st.divider()


# ==========================================================
# DESCRIPCIÓN GENERAL
# ==========================================================

bloque_informativo(

    "Objetivo del Proyecto",

    """
    Desarrollar una aplicación web interactiva orientada a la
    Ingeniería de Petróleo, integrando cálculos técnicos de
    Producción, Perforación y Reservorios mediante Python
    y Streamlit.

    La aplicación incorpora HTML, CSS, JavaScript y
    visualizaciones interactivas con Plotly.
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

    st.html(
        """
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
            </div>

            <div class="home-card-separator"></div>

            <div class="home-card-subtitle">
                Modelo técnico
            </div>

            <div class="home-card-model">
                Región Lineal + Vogel
            </div>

        </div>
        """
    )


# ==========================================================
# PERFORACIÓN
# ==========================================================

with col2:

    st.html(
        """
        <div class="home-card">

            <div class="home-card-icon">
                🏗️
            </div>

            <div class="home-card-title">
                PERFORACIÓN
            </div>

            <div class="home-card-text">
                Cálculo del gradiente y presión
                hidrostática del fluido de perforación.
            </div>

            <div class="home-card-separator"></div>

            <div class="home-card-subtitle">
                Análisis técnico
            </div>

            <div class="home-card-model">
                Sobrebalance · Balance · Bajo balance
            </div>

        </div>
        """
    )


# ==========================================================
# RESERVORIOS
# ==========================================================

with col3:

    st.html(
        """
        <div class="home-card">

            <div class="home-card-icon">
                🪨
            </div>

            <div class="home-card-title">
                RESERVORIOS
            </div>

            <div class="home-card-text">
                Estimación volumétrica del Petróleo
                Original en Sitio.
            </div>

            <div class="home-card-separator"></div>

            <div class="home-card-subtitle">
                Modelo técnico
            </div>

            <div class="home-card-model">
                POES + Volumen Recuperable
            </div>

        </div>
        """
    )


# ==========================================================
# INDICACIÓN PARA EL USUARIO
# ==========================================================

st.write("")


st.info(
    "📊 Seleccione **Ejercicios** en el menú lateral "
    "para acceder a Producción, Perforación y Reservorios."
)


# ==========================================================
# TECNOLOGÍAS UTILIZADAS
# ==========================================================

st.subheader(
    "💻 Tecnologías Utilizadas"
)


col4, col5, col6, col7 = st.columns(4)


# ==========================================================
# PYTHON
# ==========================================================

with col4:

    st.html(
        """
        <div class="tech-card">

            <div class="tech-icon">
                🐍
            </div>

            <div class="tech-title">
                Python
            </div>

            <div class="tech-text">
                Lógica y cálculos de ingeniería
            </div>

        </div>
        """
    )


# ==========================================================
# STREAMLIT
# ==========================================================

with col5:

    st.html(
        """
        <div class="tech-card">

            <div class="tech-icon">
                🎈
            </div>

            <div class="tech-title">
                Streamlit
            </div>

            <div class="tech-text">
                Desarrollo de la aplicación web
            </div>

        </div>
        """
    )


# ==========================================================
# HTML + CSS
# ==========================================================

with col6:

    st.html(
        """
        <div class="tech-card">

            <div class="tech-icon">
                🎨
            </div>

            <div class="tech-title">
                HTML + CSS
            </div>

            <div class="tech-text">
                Diseño y componentes personalizados
            </div>

        </div>
        """
    )


# ==========================================================
# JAVASCRIPT
# ==========================================================

with col7:

    st.html(
        """
        <div class="tech-card">

            <div class="tech-icon">
                ⚡
            </div>

            <div class="tech-title">
                JavaScript
            </div>

            <div class="tech-text">
                Interacciones dinámicas
            </div>

        </div>
        """
    )


# ==========================================================
# JAVASCRIPT INTERACTIVO
# ==========================================================

st.write("")

st.subheader(
    "⚡ Componente Interactivo con JavaScript"
)


st.write(
    "El siguiente componente demuestra una interacción "
    "visible implementada mediante JavaScript."
)


componente_javascript()


# ==========================================================
# PIE DE PÁGINA
# ==========================================================

st.divider()


st.html(
    """
    <div class="footer-oil">

        <div class="footer-title">
            BOOTCAMP DATA ANALYTICS FOR OIL & GAS
        </div>

        <div class="footer-text">
            Tarea Evaluativa – Módulo 1
        </div>

        <div class="footer-text">
            Aplicación desarrollada con Python + Streamlit
        </div>

    </div>
    """
)
