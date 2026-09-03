import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go


def show():

    st.header("🛢️ IPR Compuesta - Producción")

    st.write(
        "Calculadora de desempeño de afluencia para un yacimiento "
        "de petróleo subsaturado."
    )

    # ==========================================================
    # PARÁMETROS DEL RESERVORIO
    # ==========================================================

    with st.sidebar.expander(
        "🛠️ Parámetros de Producción",
        expanded=True
    ):

        p_res = st.number_input(
            "Presión de Reservorio (Pr) [psi]",
            value=3000.0,
            step=100.0
        )

        ip = st.number_input(
            "Índice de Productividad (J) [STB/d/psi]",
            value=1.5,
            step=0.1
        )

        p_bur = st.number_input(
            "Presión de Burbuja (Pb) [psi]",
            value=500.0,
            step=10.0
        )

        p_wf = st.number_input(
            "Presión de Fondo Fluyente (Pwf) [psi]",
            value=500.0,
            step=10.0
        )


    # ==========================================================
    # VALIDACIONES
    # ==========================================================

    if p_res <= 0:
        st.error(
            "⚠️ La presión del reservorio debe ser mayor que cero."
        )
        return

    if p_bur <= 0:
        st.error(
            "⚠️ La presión de burbuja debe ser mayor que cero."
        )
        return

    if ip <= 0:
        st.error(
            "⚠️ El índice de productividad debe ser mayor que cero."
        )
        return

    if p_wf < 0:
        st.error(
            "⚠️ La presión de fondo fluyente no puede ser negativa."
        )
        return

    if p_bur >= p_res:
        st.error(
            "⚠️ Para un reservorio subsaturado debe cumplirse:"
            " Pr > Pb."
        )
        return

    if p_wf > p_res:
        st.error(
            "⚠️ La presión de fondo fluyente Pwf no puede ser "
            "mayor que la presión del reservorio Pr."
        )
        return


    # ==========================================================
    # CAUDAL A LA PRESIÓN DE BURBUJA
    # qb = J * (Pr - Pb)
    # ==========================================================

    q_bur = ip * (p_res - p_bur)


    # ==========================================================
    # CAUDAL MÁXIMO TEÓRICO
    #
    # qmax = qb + (J * Pb / 1.8)
    # ==========================================================

    q_max = q_bur + (ip * p_bur / 1.8)


    # ==========================================================
    # CÁLCULO DEL CAUDAL PARA EL Pwf INGRESADO
    # ==========================================================

    if p_wf >= p_bur:

        # ------------------------------------------------------
        # REGIÓN LINEAL
        #
        # qo = J * (Pr - Pwf)
        # ------------------------------------------------------

        q_o = ip * (p_res - p_wf)

        condicion = "Por encima de la presión de burbuja"

    else:

        # ------------------------------------------------------
        # REGIÓN VOGEL
        #
        # qo = qb + (J*Pb/1.8) *
        # [1 - 0.2(Pwf/Pb) - 0.8(Pwf/Pb)^2]
        # ------------------------------------------------------

        relacion_presion = p_wf / p_bur

        q_o = q_bur + (
            (ip * p_bur / 1.8)
            *
            (
                1
                - 0.2 * relacion_presion
                - 0.8 * relacion_presion**2
            )
        )

        condicion = "Por debajo de la presión de burbuja"


    # ==========================================================
    # RESULTADOS
    # ==========================================================

    st.subheader("📊 Resultados")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Caudal de petróleo qo",
            f"{q_o:,.2f} STB/d"
        )

    with col2:

        st.metric(
            "Caudal a Pb (qb)",
            f"{q_bur:,.2f} STB/d"
        )

    with col3:

        st.metric(
            "Caudal máximo teórico",
            f"{q_max:,.2f} STB/d"
        )


    # ==========================================================
    # INDICADOR VISUAL DEL RÉGIMEN
    # ==========================================================

    if p_wf >= p_bur:

        st.success(
            "🟢 Pwf ≥ Pb → La producción se encuentra "
            "en la región LINEAL de la IPR."
        )

    else:

        st.warning(
            "🟡 Pwf < Pb → La producción se encuentra "
            "en la región NO LINEAL de Vogel."
        )


    # ==========================================================
    # GENERACIÓN DE LA CURVA IPR COMPLETA
    # ==========================================================

    # Se generan valores de Pwf desde Pr hasta 0 psi

    pwf_vector = np.linspace(
        p_res,
        0,
        200
    )

    caudales = []


    # ==========================================================
    # CALCULAR q PARA CADA VALOR DE Pwf
    # ==========================================================

    for presion in pwf_vector:

        if presion >= p_bur:

            # Región lineal

            q = ip * (
                p_res - presion
            )

        else:

            # Región Vogel

            relacion = presion / p_bur

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


    # Convertir lista a array NumPy

    caudales = np.array(caudales)


    # ==========================================================
    # DATAFRAME CON PANDAS
    # ==========================================================

    dataFrame = pd.DataFrame({

        "Pwf [psi]": pwf_vector,

        "Caudal [STB/d]": caudales

    })


    # ==========================================================
    # GRÁFICO INTERACTIVO PLOTLY
    # ==========================================================

    fig = go.Figure()


    # ----------------------------------------------------------
    # CURVA IPR
    # ----------------------------------------------------------

    fig.add_trace(
        go.Scatter(

            x=caudales,

            y=pwf_vector,

            mode="lines",

            name="IPR Compuesta",

            line=dict(
                color="#00FF90",
                width=3.5
            )

        )
    )


    # ----------------------------------------------------------
    # PUNTO SELECCIONADO POR EL USUARIO
    # ----------------------------------------------------------

    fig.add_trace(
        go.Scatter(

            x=[q_o],

            y=[p_wf],

            mode="markers",

            name="Punto de Operación",

            marker=dict(
                color="red",
                size=12
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
                size=11
            )

        )
    )


    # ----------------------------------------------------------
    # LÍNEA DE PRESIÓN DE BURBUJA
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

        title="Curva IPR Compuesta",

        xaxis_title=(
            "Caudal de Petróleo qo [STB/d]"
        ),

        yaxis_title=(
            "Presión de Fondo Fluyente Pwf [psi]"
        ),

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
    # MOSTRAR DATOS DE LA CURVA
    # ==========================================================

    with st.expander(
        "📋 Ver datos de la curva IPR"
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
# EJECUTAR PÁGINA
# ==============================================================

show()
