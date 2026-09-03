import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

from componentes import tarjeta_resultado


def show():

    # ==========================================================
    # ENCABEZADO
    # ==========================================================

    st.header(
        "🛢️ Producción – IPR Compuesta"
    )

    st.write(
        "Calculadora de desempeño de afluencia "
        "para un yacimiento de petróleo "
        "inicialmente subsaturado."
    )


    # ==========================================================
    # PARÁMETROS DE PRODUCCIÓN
    # ==========================================================

    with st.expander(
        "🛠️ Parámetros de Producción",
        expanded=True
    ):

        col1, col2 = st.columns(2)


        with col1:

            p_res = st.number_input(
                "Presión de Reservorio (Pr) [psi]",
                value=3000.0,
                step=100.0,
                key="prod_p_res"
            )


            ip = st.number_input(
                "Índice de Productividad (J) [STB/d/psi]",
                value=1.5,
                step=0.1,
                key="prod_ip"
            )


        with col2:

            p_bur = st.number_input(
                "Presión de Burbuja (Pb) [psi]",
                value=500.0,
                step=10.0,
                key="prod_p_bur"
            )


            p_wf = st.number_input(
                "Presión de Fondo Fluyente (Pwf) [psi]",
                value=500.0,
                step=10.0,
                key="prod_p_wf"
            )


    # ==========================================================
    # VALIDACIONES
    # ==========================================================

    if p_res <= 0:

        st.error(
            "⚠️ Pr debe ser mayor que cero."
        )

        return


    if ip <= 0:

        st.error(
            "⚠️ J debe ser mayor que cero."
        )

        return


    if p_bur <= 0:

        st.error(
            "⚠️ Pb debe ser mayor que cero."
        )

        return


    if p_bur >= p_res:

        st.error(
            "⚠️ Para el reservorio subsaturado "
            "debe cumplirse Pr > Pb."
        )

        return


    if p_wf < 0:

        st.error(
            "⚠️ Pwf no puede ser negativa."
        )

        return


    if p_wf > p_res:

        st.error(
            "⚠️ Pwf no puede ser mayor que Pr."
        )

        return


    # ==========================================================
    # CAUDAL A Pb
    # ==========================================================

    q_bur = ip * (
        p_res - p_bur
    )


    # ==========================================================
    # CAUDAL MÁXIMO
    # ==========================================================

    q_max = q_bur + (
        ip * p_bur / 1.8
    )


    # ==========================================================
    # CAUDAL PARA Pwf INGRESADO
    # ==========================================================

    if p_wf >= p_bur:

        q_o = ip * (
            p_res - p_wf
        )

        condicion = (
            "Región Lineal"
        )


    else:

        relacion_presion = (
            p_wf / p_bur
        )

        q_o = q_bur + (

            (ip * p_bur / 1.8)

            *

            (
                1
                - 0.2 * relacion_presion
                - 0.8 * relacion_presion**2
            )

        )

        condicion = (
            "Región Vogel"
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
            "Caudal de Petróleo",
            f"{q_o:,.2f}",
            "STB/d",
            "🛢️"
        )


    with col2:

        tarjeta_resultado(
            "Caudal a Pb",
            f"{q_bur:,.2f}",
            "STB/d",
            "📍"
        )


    with col3:

        tarjeta_resultado(
            "Caudal Máximo",
            f"{q_max:,.2f}",
            "STB/d",
            "📈"
        )


    # ==========================================================
    # CONDICIÓN DE OPERACIÓN
    # ==========================================================

    if p_wf >= p_bur:

        st.success(
            "🟢 Pwf ≥ Pb → Región Lineal."
        )

    else:

        st.warning(
            "🟡 Pwf < Pb → Región Vogel."
        )


    st.info(
        f"Condición actual: **{condicion}**"
    )


    # ==========================================================
    # CURVA IPR
    # ==========================================================

    pwf_vector = np.linspace(
        p_res,
        0,
        200
    )


    caudales = []


    for presion in pwf_vector:

        if presion >= p_bur:

            q = ip * (
                p_res - presion
            )


        else:

            relacion = (
                presion / p_bur
            )


            q = q_bur + (

                (ip * p_bur / 1.8)

                *

                (
                    1
                    - 0.2 * relacion
                    - 0.8 * relacion**2
                )

            )


        caudales.append(q)


    caudales = np.array(
        caudales
    )


    region_lineal = (
        pwf_vector >= p_bur
    )


    region_vogel = (
        pwf_vector < p_bur
    )


    # ==========================================================
    # DATAFRAME
    # ==========================================================

    dataFrame = pd.DataFrame({

        "Pwf [psi]":
            pwf_vector,

        "Caudal [STB/d]":
            caudales

    })


    # ==========================================================
    # GRÁFICO
    # ==========================================================

    fig = go.Figure()


    fig.add_trace(
        go.Scatter(

            x=caudales[
                region_lineal
            ],

            y=pwf_vector[
                region_lineal
            ],

            mode="lines",

            name="Región Lineal",

            line=dict(
                color="#00FF90",
                width=4
            )

        )
    )


    fig.add_trace(
        go.Scatter(

            x=caudales[
                region_vogel
            ],

            y=pwf_vector[
                region_vogel
            ],

            mode="lines",

            name="Región Vogel",

            line=dict(
                color="#FFD166",
                width=4
            )

        )
    )


    # Punto operativo

    fig.add_trace(
        go.Scatter(

            x=[q_o],

            y=[p_wf],

            mode="markers",

            name="Punto de Operación",

            marker=dict(
                color="red",
                size=13
            )

        )
    )


    # Punto de burbuja

    fig.add_trace(
        go.Scatter(

            x=[q_bur],

            y=[p_bur],

            mode="markers",

            name="Punto de Burbuja",

            marker=dict(
                color="yellow",
                size=12
            )

        )
    )


    fig.add_hline(

        y=p_bur,

        line_dash="dash",

        annotation_text="Pb"

    )


    fig.update_layout(

        title=(
            "Curva IPR Compuesta"
        ),

        xaxis_title=(
            "Caudal qo [STB/d]"
        ),

        yaxis_title=(
            "Pwf [psi]"
        ),

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
        "📋 Ver datos de la curva IPR"
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
            "### Caudal a Pb"
        )

        st.latex(
            r"q_b = J(P_r-P_b)"
        )


        st.write(
            "### Pwf ≥ Pb"
        )

        st.latex(
            r"q_o = J(P_r-P_{wf})"
        )


        st.write(
            "### Pwf < Pb"
        )

        st.latex(
            r"""
            q_o =
            q_b +
            \frac{J P_b}{1.8}
            \left[
            1
            -0.2
            \left(
            \frac{P_{wf}}{P_b}
            \right)
            -0.8
            \left(
            \frac{P_{wf}}{P_b}
            \right)^2
            \right]
            """
        )


        st.write(
            "### Caudal máximo"
        )

        st.latex(
            r"""
            q_{o,max}
            =
            q_b
            +
            \frac{J P_b}{1.8}
            """
        )


if __name__ == "__main__":
    show()
