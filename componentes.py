import streamlit as st
import textwrap


# ==========================================================
# TARJETA DE RESULTADOS
# ==========================================================

def tarjeta_resultado(
    titulo,
    valor,
    unidad,
    icono="📊"
):

    html_tarjeta = f"""
<div class="oil-card">
    <div class="oil-card-icon">{icono}</div>
    <div class="oil-card-title">{titulo}</div>
    <div class="oil-card-value">{valor}</div>
    <div class="oil-card-unit">{unidad}</div>
</div>
"""

    st.markdown(
        textwrap.dedent(
            html_tarjeta
        ),
        unsafe_allow_html=True
    )


# ==========================================================
# BLOQUE INFORMATIVO
# ==========================================================

def bloque_informativo(
    titulo,
    texto,
    icono="ℹ️"
):

    html_bloque = f"""
<div class="technical-info">
    <strong>{icono} {titulo}</strong>
    <br><br>
    {texto}
</div>
"""

    st.markdown(
        textwrap.dedent(
            html_bloque
        ),
        unsafe_allow_html=True
    )
