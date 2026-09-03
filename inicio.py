import streamlit as st

from estilos import cargar_estilos


# ==========================================================
# CARGAR ESTILOS GENERALES
# ==========================================================

cargar_estilos()


# ==========================================================
# ENCABEZADO PRINCIPAL
# ==========================================================

st.title(
    "🛢️ Oil & Gas Engineering Dashboard"
)

st.subheader(
    "Tarea Evaluativa – Módulo 1"
)

st.write(
    """
    Aplicación interactiva desarrollada con Python y Streamlit
    para resolver y analizar problemas fundamentales de
    Ingeniería de Producción, Perforación y Reservorios.
    """
)


# ==========================================================
# INFORMACIÓN GENERAL
# ==========================================================

st.markdown(
    """
    <div class="technical-info">

        <b>🎯 Objetivo de la aplicación</b>

        <br><br>

        Integrar cálculos técnicos de Ingeniería de Petróleo
        en una interfaz web interactiva que permita modificar
        parámetros, analizar resultados y visualizar el
        comportamiento de cada modelo.

    </div>
    """,
    unsafe_allow_html=True
)


# ==========================================================
# MÓDULOS DISPONIBLES
# ==========================================================

st.subheader(
    "📚 Módulos disponibles"
)


col1, col2, col3 = st.columns(3)


# ==========================================================
# PRODUCCIÓN
# ==========================================================

with col1:

    st.markdown(
        """
        <div class="oil-card">

            <div class="oil-card-icon">
                🛢️
            </div>

            <div class="oil-card-title">
                PRODUCCIÓN
            </div>

            <div class="oil-card-value">
                IPR Compuesta
            </div>

            <div class="oil-card-unit">
                Región Lineal + Vogel
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================================
# PERFORACIÓN
# ==========================================================

with col2:

    st.markdown(
        """
        <div class="oil-card">

            <div class="oil-card-icon">
                🏗️
            </div>

            <div class="oil-card-title">
                PERFORACIÓN
            </div>

            <div class="oil-card-value">
                Presión Hidrostática
            </div>

            <div class="oil-card-unit">
                PH – Gradiente – Balance
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================================
# RESERVORIOS
# ==========================================================

with col3:

    st.markdown(
        """
        <div class="oil-card">

            <div class="oil-card-icon">
                🪨
            </div>

            <div class="oil-card-title">
                RESERVORIOS
            </div>

            <div class="oil-card-value">
                POES
            </div>

            <div class="oil-card-unit">
                Volumétrico + Recuperable
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================================
# ESPACIO
# ==========================================================

st.write("")


# ==========================================================
# ACCESO A LOS EJERCICIOS
# ==========================================================

st.page_link(
    "ejercicios.py",
    label="📊 Abrir Ejercicios de Ingeniería de Petróleo",
    icon="📊",
    use_container_width=True
)


# ==========================================================
# INFORMACIÓN DE NAVEGACIÓN
# ==========================================================

st.info(
    "ℹ️ En la sección Ejercicios encontrarás los módulos "
    "de Producción, Perforación y Reservorios organizados "
    "mediante pestañas."
)
