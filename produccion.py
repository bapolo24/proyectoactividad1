import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

from componentes import tarjeta_resultado
from estilos import cargar_estilos


def show():

    # ==========================================================
    # CARGAR ESTILOS
    # ==========================================================

    cargar_estilos()


    # ==========================================================
    # ENCABEZADO
    # ==========================================================

    st.header("🛢️ Producción – IPR Compuesta")

    st.write(
        "Calculadora de desempeño de afluencia para un yacimiento "
        "de petróleo inicialmente subsaturado."
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
            "⚠️ La presión del reservorio debe ser mayor que cero."
        )

        return


    if ip <= 0:

        st.error(
            "⚠️ El índice de productividad debe ser mayor que cero."
        )

        return


    if p_bur <= 0:

        st.error(
            "⚠️ La presión de burbuja debe ser mayor que cero."
        )

        return


    if p_bur >= p_res:

        st.error(
            "⚠️ Para un reservorio inicialmente subsaturado "
            "debe cumplirse Pr > Pb."
        )

        return


    if p_wf < 0:

        st.error(
            "⚠️ La presión de fondo fluyente no puede ser negativa."
        )

        return


    if p_wf > p_res:

        st.error(
            "⚠️ Pwf no puede ser mayor que Pr."
        )

        return


    # ==========================================================
    # CAUDAL A LA PRESIÓN DE BURBUJA
    #
    # qb = J * (Pr - Pb)
    # ==========================================================

    q_bur = ip * (p_res - p_bur)


    # ==========================================================
    # CAUDAL MÁXIMO TEÓRICO
    #
    # qmax = qb + (J * Pb / 1.8)
    # ==========================================================

    q_max = q_bur + (
        ip * p_bur / 1.8
    )


    # ==========================================================
    # CÁLCULO DEL CAUDAL DE OPERACIÓN
    # ==========================================================

    if p_wf >= p_bur:

        q_o = ip * (
            p_res - p_wf
        )

        condicion = (
            "Región lineal – Pwf ≥ Pb"
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
            "Región Vogel – Pwf < Pb"
        )


    # ==========================================================
    # RESULTADOS CON TARJETAS PERSONALIZADAS
    # ==========================================================

    st.subheader("📊 Resultados")

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
    # INDICADOR VISUAL DEL RÉGIMEN
    # ==========================================================

    if p_wf >= p_bur:

        st.success(
            "🟢 REGIÓN LINEAL: Pwf ≥ Pb. "
            "El petróleo se encuentra por encima "
            "de la presión de burbuja."
        )

    else:

        st.warning(
            "🟡 REGIÓN VOGEL: Pwf < Pb. "
            "Existe liberación de gas y la relación "
            "caudal-presión deja de ser lineal."
        )


    st.info(
        f"Condición de operación: **{condicion}**"
    )


    # ==========================================================
    # GENERACIÓN DE CURVA IPR
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


    # ==========================================================
    # IDENTIFICAR REGIONES
    # ==========================================================

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
    # GRÁFICO PLOTLY
    # ==========================================================

    fig = go.Figure()


    # ----------------------------------------------------------
    # REGIÓN LINEAL
    # ----------------------------------------------------------

    fig.add_trace(
        go.Scatter(

            x=caudales[region_lineal],

            y=pwf_vector[region_lineal],

            mode="lines",

            name="Región Lineal",

            line=dict(
                color="#00FF90",
                width=4
            )

        )
    )


    # ----------------------------------------------------------
    # REGIÓN VOGEL
    # ----------------------------------------------------------

    fig.add_trace(
        go.Scatter(

            x=caudales[region_vogel],

            y=pwf_vector[region_vogel],

            mode="lines",

            name="Región Vogel",

            line=dict(
                color="#FFD166",
                width=4
            )

        )
    )


    # ----------------------------------------------------------
    # PUNTO DE OPERACIÓN
    # ----------------------------------------------------------

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


    # ----------------------------------------------------------
    # PUNTO DE BURBUJA
    # ----------------------------------------------------------

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


    # ----------------------------------------------------------
    # LÍNEA Pb
    # ----------------------------------------------------------

    fig.add_hline(

        y=p_bur,

        line_dash="dash",

        annotation_text="Pb",

        annotation_position="top right"

    )


    # ==========================================================
    # CONFIGURACIÓN DEL GRÁFICO
    # ==========================================================

    fig.update_layout(

        title=(
            "Curva IPR Compuesta "
            "– Región Lineal + Vogel"
        ),

        xaxis_title=(
            "Caudal de Petróleo qo [STB/d]"
        ),

        yaxis_title=(
            "Presión de Fondo Fluyente "
            "Pwf [psi]"
        ),

        template="plotly_dark",

        hovermode="closest",

        height=600

    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # ==========================================================
    # TABLA DE DATOS
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
            "### Caudal a la presión de burbuja"
        )

        st.latex(
            r"q_b = J(P_r-P_b)"
        )


        st.write(
            "### Para Pwf ≥ Pb"
        )

        st.latex(
            r"q_o = J(P_r-P_{wf})"
        )


        st.write(
            "### Para Pwf < Pb"
        )

        st.latex(
            r"""
            q_o =
            q_b +
            \frac{J P_b}{1.8}
            \left[
            1
            -0.2\left(\frac{P_{wf}}{P_b}\right)
            -0.8\left(\frac{P_{wf}}{P_b}\right)^2
            \right]
            """
        )


        st.write(
            "### Caudal máximo teórico"
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


# ==============================================================
# EJECUCIÓN INDIVIDUAL PARA PRUEBAS
# ==============================================================

if __name__ == "__main__":
    show()
