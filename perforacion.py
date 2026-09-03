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
        "🏗️ Perforación – Presión Hidrostática"
    )

    st.write(
        "Calculadora de presión hidrostática "
        "durante la perforación."
    )


    st.info(
        "ℹ️ La presión hidrostática depende de TVD "
        "y no de MD, debido a que depende de la altura "
        "vertical de la columna de fluido."
    )


    # ==========================================================
    # PARÁMETROS
    # ==========================================================

    with st.expander(
        "🛠️ Parámetros de Perforación",
        expanded=True
    ):

        col1, col2 = st.columns(2)


        with col1:

            MW = st.number_input(
                "Peso de Lodo (MW) [ppg]",
                value=10.0,
                step=0.1,
                key="perf_MW"
            )


            MD = st.number_input(
                "Profundidad Medida (MD) [ft]",
                value=10000.0,
                step=100.0,
                key="perf_MD"
            )


        with col2:

            TVD = st.number_input(
                "Profundidad Vertical Verdadera (TVD) [ft]",
                value=9000.0,
                step=100.0,
                key="perf_TVD"
            )


            p_formacion = st.number_input(
                "Presión de Formación (Pform) [psi]",
                value=4500.0,
                step=100.0,
                key="perf_p_formacion"
            )


    # ==========================================================
    # VALIDACIONES
    # ==========================================================

    if MW <= 0:

        st.error(
            "⚠️ MW debe ser mayor que cero."
        )

        return


    if MD <= 0:

        st.error(
            "⚠️ MD debe ser mayor que cero."
        )

        return


    if TVD <= 0:

        st.error(
            "⚠️ TVD debe ser mayor que cero."
        )

        return


    if TVD > MD:

        st.error(
            "⚠️ Debe cumplirse TVD ≤ MD."
        )

        return


    if p_formacion < 0:

        st.error(
            "⚠️ La presión de formación "
            "no puede ser negativa."
        )

        return


    # ==========================================================
    # CÁLCULOS
    # ==========================================================

    GRAD_H = (
        0.052 * MW
    )


    PH = (
        0.052
        * MW
        * TVD
    )


    DIF_P = (
        PH
        - p_formacion
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
            "Gradiente Hidrostático",
            f"{GRAD_H:.3f}",
            "psi/ft",
            "📐"
        )


    with col2:

        tarjeta_resultado(
            "Presión Hidrostática",
            f"{PH:,.2f}",
            "psi",
            "🏗️"
        )


    with col3:

        tarjeta_resultado(
            "Diferencial de Presión",
            f"{DIF_P:,.2f}",
            "psi",
            "⚖️"
        )


    # ==========================================================
    # BALANCE
    # ==========================================================

    tolerancia_balance = 50.0


    if DIF_P > tolerancia_balance:

        st.success(
            "🟢 SOBREBALANCE: PH > Pform."
        )


    elif DIF_P < -tolerancia_balance:

        st.error(
            "🔴 BAJO BALANCE: PH < Pform."
        )


    else:

        st.warning(
            "🟡 BALANCE APROXIMADO: PH ≈ Pform."
        )


    st.caption(
        "Se considera ±50 psi como tolerancia "
        "para el indicador de balance aproximado."
    )


    # ==========================================================
    # CURVA PH VS TVD
    # ==========================================================

    TVDS = np.linspace(
        0,
        TVD,
        200
    )


    PH_vector = (
        0.052
        * MW
        * TVDS
    )


    # ==========================================================
    # DATAFRAME
    # ==========================================================

    dataFrame = pd.DataFrame({

        "TVD [ft]":
            TVDS,

        "PH [psi]":
            PH_vector

    })


    # ==========================================================
    # GRÁFICO
    # ==========================================================

    fig = go.Figure()


    fig.add_trace(
        go.Scatter(

            x=TVDS,

            y=PH_vector,

            mode="lines",

            name="PH vs TVD",

            line=dict(
                color="#00FF90",
                width=4
            )

        )
    )


    fig.add_trace(
        go.Scatter(

            x=[TVD],

            y=[PH],

            mode="markers",

            name="Punto Calculado",

            marker=dict(
                color="red",
                size=13
            )

        )
    )


    fig.add_hline(

        y=p_formacion,

        line_dash="dash",

        line_color="#FFD166",

        annotation_text=(
            f"Pform = "
            f"{p_formacion:,.0f} psi"
        )

    )


    fig.update_layout(

        title=(
            "Presión Hidrostática vs TVD"
        ),

        xaxis_title="TVD [ft]",

        yaxis_title="PH [psi]",

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
        "📋 Ver datos de PH vs TVD"
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
            "### Gradiente Hidrostático"
        )

        st.latex(
            r"G_h = 0.052 \times MW"
        )


        st.write(
            "### Presión Hidrostática"
        )

        st.latex(
            r"P_h = 0.052 \times MW \times TVD"
        )


        st.write(
            "### Diferencial de Presión"
        )

        st.latex(
            r"\Delta P = P_h - P_{form}"
        )


if __name__ == "__main__":
    show()
