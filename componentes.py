import streamlit as st


# ==========================================================
# TARJETA PERSONALIZADA DE RESULTADOS
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

    st.html(html_tarjeta)


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
        <div class="technical-info-title">
            {icono} {titulo}
        </div>

        <div class="technical-info-text">
            {texto}
        </div>
    </div>
    """

    st.html(html_bloque)
