import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from componentes import tarjeta_resultado


def show():

    # ==========================================================
    # ENCABEZADO
    # ==========================================================

    st.header(
        "🪨 Reservorios – Estimación Volumétrica del POES"
    )


    st.write(
        "Calculadora volumétrica para estimar "
        "el Petróleo Original en Sitio (POES) "
        "y el volumen recuperable."
    )


    # ==========================================================
    # PARÁMETROS
    # ==========================================================

    with st.expander(
        "🪨 Parámetros del Reservorio",
        expanded=True
    ):

        col1, col2 = st.columns(2)


        with col1:

            A = st.number_input(
                "Área del Reservorio (A) [acres]",
                value=1800.0,
                step=100.0,
                key="res_A"
            )


            h = st.number_input(
                "Espesor Bruto (h) [ft]",
                value=70.0,
                step=5.0,
                key="res_h"
            )


            NTG = st.number_input(
                "Net-to-Gross (NTG) [fracción]",
                value=0.80,
                step=0.01,
                format="%.2f",
                key="res_NTG"
            )


            poro = st.number_input(
                "Porosidad Efectiva (poro) [fracción]",
                value=0.20,
                step=0.01,
                format="%.2f",
                key="res_poro"
            )


        with col2:

            Swi = st.number_input(
                "Saturación Inicial de Agua (Swi) [fracción]",
                value=0.20,
                step=0.01,
                format="%.2f",
                key="res_Swi"
            )


            Boi = st.number_input(
                "Factor Volumétrico Inicial "
                "(Boi) [rb/STB]",
                value=1.20,
                step=0.01,
                format="%.2f",
                key="res_Boi"
            )


            FR = st.number_input(
                "Factor de Recobro (FR) [fracción]",
                value=0.30,
                step=0.01,
                format="%.2f",
                key="res_FR"
            )


        st.caption(
            "NTG, porosidad, Swi y FR deben "
            "ingresarse como fracciones. "
            "Ejemplo: 20 % = 0.20."
        )


    # ==========================================================
    # VALIDACIONES
    # ==========================================================

    if A <= 0:

        st.error(
            "⚠️ A debe ser mayor que cero."
        )

        return


    if h <= 0:

        st.error(
            "⚠️ h debe ser mayor que cero."
        )

        return


    if NTG < 0 or NTG > 1:

        st.error(
            "⚠️ NTG debe estar entre 0 y 1."
        )

        return


    if poro < 0 or poro > 1:

        st.error(
            "⚠️ La porosidad debe estar "
            "entre 0 y 1."
        )

        return


    if Swi < 0 or Swi > 1:

        st.error(
            "⚠️ Swi debe estar entre 0 y 1."
        )

        return


    if Boi <= 0:

        st.error(
            "⚠️ Boi debe ser mayor que cero."
        )

        return


    if FR < 0 or FR > 1:

        st.error(
            "⚠️ FR debe estar entre 0 y 1."
        )

        return


    # ==========================================================
    # CÁLCULOS
    # ==========================================================

    So = (
        1 - Swi
    )


    h_n = (
        h * NTG
    )


    POES = (

        7758

        * A

        * h_n

        * poro

        * (1 - Swi)

        / Boi

    )


    POES_MMSTB = (
        POES
        / 1_000_000
    )


    RECUPERABLE = (
        POES
        * FR
    )


    RECUPERABLE_MMSTB = (
        RECUPERABLE
        / 1_000_000
    )


    # ==========================================================
    # RESULTADOS
    # ==========================================================

    st.subheader(
        "📊 Resultados"
    )


    col1, col2, col3 = st.columns(3)


    with col1:

        tarjeta_resultado(
            "Espesor Neto",
            f"{h_n:,.2f}",
            "ft",
            "📏"
        )


    with col2:

        tarjeta_resultado(
            "POES",
            f"{POES_MMSTB:,.2f}",
            "MMSTB",
            "🛢️"
        )


    with col3:

        tarjeta_resultado(
            "Volumen Recuperable",
            f"{RECUPERABLE_MMSTB:,.2f}",
            "MMSTB",
            "📊"
        )


    col4, col5, col6 = st.columns(3)


    with col4:

        tarjeta_resultado(
            "POES",
            f"{POES:,.0f}",
            "STB",
            "🛢️"
        )


    with col5:

        tarjeta_resultado(
            "Petróleo Recuperable",
            f"{RECUPERABLE:,.0f}",
            "STB",
            "📈"
        )


    with col6:

        tarjeta_resultado(
            "Saturación de Petróleo",
            f"{So * 100:.1f}",
            "%",
            "💧"
        )


    # ==========================================================
    # INTERPRETACIÓN
    # ==========================================================

    st.success(
        f"🟢 Con un factor de recobro de "
        f"{FR * 100:.1f} %, se estima un volumen "
        f"recuperable de "
        f"{RECUPERABLE_MMSTB:,.2f} MMSTB."
    )


    # ==========================================================
    # DATAFRAME
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
    # GRÁFICO
    # ==========================================================

    fig = go.Figure()


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

            text=[
                f"{POES_MMSTB:,.2f} MMSTB",
                f"{RECUPERABLE_MMSTB:,.2f} MMSTB"
            ],

            textposition="auto",

            marker=dict(

                color=[
                    "#00A6FB",
                    "#00CC96"
                ]

            )

        )
    )


    fig.update_layout(

        title=(
            "POES vs Petróleo Recuperable"
        ),

        xaxis_title="Volumen",

        yaxis_title="MMSTB",

        template="plotly_dark",

        height=600

    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # ==========================================================
    # TABLA
    # ==========================================================

    with st.expander(
        "📋 Ver resultados volumétricos"
    ):

        st.dataframe(
            dataFrame,
            use_container_width=True
        )


    # ==========================================================
    # ECUACIONES
    # ==========================================================

    with st.expander(
        "🧮 Ver ecuaciones utilizadas"
    ):

        st.write(
            "### Espesor Neto"
        )

        st.latex(
            r"h_n = h \times NTG"
        )


        st.write(
            "### Saturación de Petróleo"
        )

        st.latex(
            r"S_o = 1-S_{wi}"
        )


        st.write(
            "### Petróleo Original en Sitio"
        )

        st.latex(
            r"""
            POES =
            \frac{
            7758
            \times A
            \times h_n
            \times \phi
            \times (1-S_{wi})
            }{
            B_{oi}
            }
            """
        )


        st.write(
            "### Petróleo Recuperable"
        )

        st.latex(
            r"""
            Petróleo\ Recuperable
            =
            POES \times FR
            """
        )


if __name__ == "__main__":
    show()
