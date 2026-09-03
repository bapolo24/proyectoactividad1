import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go


def show():

    st.header("🪨 Reservorios")

    st.write(
        "Calculadora volumétrica para estimar el Petróleo Original "
        "en Sitio (POES) y el volumen recuperable."
    )

    # ==========================================================
    # PARÁMETROS DEL RESERVORIO
    # ==========================================================

    with st.sidebar.expander(
        "🪨 Parámetros del Reservorio",
        expanded=True
    ):

        A = st.number_input(
            "Área del reservorio (A) [acres]",
            value=1800.0,
            step=100.0
        )

        h = st.number_input(
            "Espesor bruto (h) [ft]",
            value=70.0,
            step=5.0
        )

        NTG = st.number_input(
            "Net-to-Gross (NTG) [fracción]",
            value=0.80,
            step=0.01,
            format="%.2f"
        )

        poro = st.number_input(
            "Porosidad efectiva (poro) [fracción]",
            value=0.20,
            step=0.01,
            format="%.2f"
        )

        Swi = st.number_input(
            "Saturación inicial de agua (Swi) [fracción]",
            value=0.20,
            step=0.01,
            format="%.2f"
        )

        Boi = st.number_input(
            "Factor volumétrico inicial del petróleo (Boi) [rb/STB]",
            value=1.20,
            step=0.01,
            format="%.2f"
        )

        FR = st.number_input(
            "Factor de recobro (FR) [fracción]",
            value=0.30,
            step=0.01,
            format="%.2f"
        )


    # ==========================================================
    # VALIDACIONES
    # ==========================================================

    if A <= 0:

        st.error(
            "⚠️ El área del reservorio A debe ser mayor que cero."
        )

        return


    if h <= 0:

        st.error(
            "⚠️ El espesor bruto h debe ser mayor que cero."
        )

        return


    if NTG < 0 or NTG > 1:

        st.error(
            "⚠️ NTG debe ingresarse como fracción entre 0 y 1."
        )

        return


    if poro < 0 or poro > 1:

        st.error(
            "⚠️ La porosidad efectiva debe ingresarse como "
            "fracción entre 0 y 1."
        )

        return


    if Swi < 0 or Swi > 1:

        st.error(
            "⚠️ Swi debe ingresarse como fracción entre 0 y 1."
        )

        return


    if Boi <= 0:

        st.error(
            "⚠️ Boi debe ser mayor que cero."
        )

        return


    if FR < 0 or FR > 1:

        st.error(
            "⚠️ El factor de recobro FR debe ingresarse como "
            "fracción entre 0 y 1."
        )

        return


    # ==========================================================
    # ESPESOR NETO
    #
    # h_n = h * NTG
    # ==========================================================

    h_n = h * NTG


    # ==========================================================
    # PETRÓLEO ORIGINAL EN SITIO - POES
    #
    # POES = 7758 * A * h_n * poro * (1 - Swi) / Boi
    # ==========================================================

    POES = (
        7758
        * A
        * h_n
        * poro
        * (1 - Swi)
        / Boi
    )


    # ==========================================================
    # POES EN MILLONES DE BARRILES
    # ==========================================================

    POES_MMSTB = POES / 1_000_000


    # ==========================================================
    # PETRÓLEO RECUPERABLE ESTIMADO
    #
    # RECUPERABLE = POES * FR
    # ==========================================================

    RECUPERABLE = POES * FR


    # ==========================================================
    # PETRÓLEO RECUPERABLE EN MILLONES DE BARRILES
    # ==========================================================

    RECUPERABLE_MMSTB = RECUPERABLE / 1_000_000


    # ==========================================================
    # RESULTADOS
    # ==========================================================

    st.subheader("📊 Resultados")

    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "Espesor neto hₙ",
            f"{h_n:,.2f} ft"
        )


    with col2:

        st.metric(
            "POES",
            f"{POES_MMSTB:,.2f} MMSTB"
        )


    with col3:

        st.metric(
            "Petróleo recuperable",
            f"{RECUPERABLE_MMSTB:,.2f} MMSTB"
        )


    col4, col5 = st.columns(2)


    with col4:

        st.metric(
            "POES [STB]",
            f"{POES:,.0f} STB"
        )


    with col5:

        st.metric(
            "Recuperable [STB]",
            f"{RECUPERABLE:,.0f} STB"
        )


    # ==========================================================
    # INDICADOR VISUAL
    # ==========================================================

    st.success(
        f"🟢 Con un factor de recobro de {FR * 100:.1f} %, "
        f"el volumen recuperable estimado representa "
        f"{FR * 100:.1f} % del POES calculado."
    )


    # ==========================================================
    # DATAFRAME CON PANDAS
    # ==========================================================

    dataFrame = pd.DataFrame({

        "Volumen": [
            "POES",
            "Petróleo Recuperable"
        ],

        "STB": [
            POES,
            RECUPERABLE
        ],

        "MMSTB": [
            POES_MMSTB,
            RECUPERABLE_MMSTB
        ]

    })


    # ==========================================================
    # GRÁFICO INTERACTIVO PLOTLY
    # ==========================================================

    fig = go.Figure()


    # ----------------------------------------------------------
    # COMPARACIÓN POES VS VOLUMEN RECUPERABLE
    # ----------------------------------------------------------

    fig.add_trace(
        go.Bar(

            x=[
                "POES",
                "Petróleo Recuperable"
            ],

            y=[
                POES_MMSTB,
                RECUPERABLE_MMSTB
            ],

            name="Volumen",

            text=[
                f"{POES_MMSTB:,.2f} MMSTB",
                f"{RECUPERABLE_MMSTB:,.2f} MMSTB"
            ],

            textposition="auto"

        )
    )


    # ==========================================================
    # CONFIGURACIÓN DEL GRÁFICO
    # ==========================================================

    fig.update_layout(

        title="POES vs Petróleo Recuperable",

        xaxis_title="Volumen",

        yaxis_title="Volumen [MMSTB]",

        template="plotly_dark",

        hovermode="closest",

        height=600

    )


    # ==========================================================
    # MOSTRAR GRÁFICA
    # ==========================================================

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # ==========================================================
    # MOSTRAR TABLA DE DATOS
    # ==========================================================

    with st.expander(
        "📋 Ver resultados volumétricos"
    ):

        st.dataframe(
            dataFrame,
            use_container_width=True
        )


    # ==========================================================
    # INFORMACIÓN DEL CÁLCULO
    # ==========================================================

    with st.expander(
        "🧮 Ver ecuaciones utilizadas"
    ):

        st.write(
            "### Espesor neto hₙ"
        )

        st.latex(
            r"h_n = h \times NTG"
        )


        st.write(
            "### Petróleo Original en Sitio (POES)"
        )

        st.latex(
            r"""
            POES =
            \frac{
            7758 \times A \times h_n \times \phi
            \times (1-S_{wi})
            }{
            B_{oi}
            }
            """
        )


        st.write(
            "### Petróleo recuperable estimado"
        )

        st.latex(
            r"""
            Petróleo\ Recuperable =
            POES \times FR
            """
        )


        st.write(
            "### Conversión a MMSTB"
        )

        st.latex(
            r"""
            MMSTB =
            \frac{STB}{1{,}000{,}000}
            """
        )


# ==============================================================
# EJECUTAR PÁGINA
# ==============================================================

show()
