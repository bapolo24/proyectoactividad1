import streamlit as st


def tarjeta_resultado(
    titulo,
    valor,
    unidad,
    icono="📊"
):

    st.markdown(
        f"""
        <div class="oil-card">

            <div class="oil-card-icon">
                {icono}
            </div>

            <div class="oil-card-title">
                {titulo}
            </div>

            <div class="oil-card-value">
                {valor}
            </div>

            <div class="oil-card-unit">
                {unidad}
            </div>

        </div>
        """,

        unsafe_allow_html=True
    )


def bloque_informativo(
    titulo,
    texto,
    icono="ℹ️"
):

    st.markdown(
        f"""
        <div class="technical-info">

            <strong>
                {icono} {titulo}
            </strong>

            <br><br>

            {texto}

        </div>
        """,

        unsafe_allow_html=True
    )
