import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go


def show():

    st.header("🏗️ Perforación")

    st.write(
        "Calculadora de presión hidrostática durante la perforación."
    )

    # ==========================================================
    # PARÁMETROS DE LA PERFORACIÓN
    # ==========================================================

    with st.sidebar.expander(
        "🛠️ Parámetros de Perforación",
        expanded=True
    ):

        MW = st.number_input(
            "Peso de lodo (MW) [ppg]",
            value=20.0,
            step=1.0
        )

        MD = st.number_input(
            "Profundidad medida del pozo (MD) [ft]",
            value=20000.0,
            step=100.0
        )

        TVD = st.number_input(
            "Profundidad vertical verdadera (TVD) [ft]",
            value=500.0,
            step=10.0
        )

        p_formacion = st.number_input(
            "Presión de Formación (Pform) [psi]",
            value=6000.0,
            step=100.0
        )


    # ==========================================================
    # VALIDACIONES
    # ==========================================================

    if MW <= 0:

        st.error(
            "⚠️ El peso de lodo MW debe ser mayor que cero."
        )

        return


    if MD <= 0:

        st.error(
            "⚠️ La profundidad MD debe ser mayor que cero."
        )

        return


    if TVD <= 0:

        st.error(
            "⚠️ La profundidad TVD debe ser mayor que cero."
        )

        return


    if TVD > MD:

        st.error(
            "⚠️ La profundidad vertical verdadera TVD "
            "no puede ser mayor que la profundidad medida MD."
        )

        return


    if p_formacion < 0:

        st.error(
            "⚠️ La presión de formación no puede ser negativa."
        )

        return


    # ==========================================================
    # GRADIENTE HIDROSTÁTICO
    #
    # Gh = 0.052 * MW
    # ==========================================================

    GRAD_H = 0.052 * MW


    # ==========================================================
    # PRESIÓN HIDROSTÁTICA
    #
    # PH = 0.052 * MW * TVD
    # ==========================================================

    PH = 0.052 * MW * TVD


    # ==========================================================
    # DIFERENCIAL DE PRESIÓN
    #
    # ΔP = PH - Pform
    # ==========================================================

    DIF_P = PH - p_formacion


    # ==========================================================
    # RESULTADOS
    # ==========================================================

    st.subheader("📊 Resultados")

    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "Gradiente hidrostático",
            f"{GRAD_H:.3f} psi/ft"
        )


    with col2:

        st.metric(
            "Presión hidrostática",
            f"{PH:,.2f} psi"
        )


    with col3:

        st.metric(
            "Diferencial de presión",
            f"{DIF_P:,.2f} psi"
        )


    # ==========================================================
    # CONDICIÓN DE BALANCE
    # ==========================================================

    tolerancia_balance = 50.0


    if DIF_P > tolerancia_balance:

        st.success(
            "🟢 SOBREBALANCE: la presión hidrostática "
            "es mayor que la presión de formación."
        )


    elif DIF_P < -tolerancia_balance:

        st.error(
            "🔴 BAJO BALANCE: la presión hidrostática "
            "es menor que la presión de formación."
        )


    else:

        st.warning(
            "🟡 BALANCE APROXIMADO: la presión hidrostática "
            "es aproximadamente igual a la presión de formación."
        )


    # ==========================================================
    # GENERACIÓN DE PH VS TVD
    # ==========================================================

    TVDS = np.linspace(
        0,
        TVD,
        200
    )


    PH_vector = 0.052 * MW * TVDS


    # ==========================================================
    # DATAFRAME CON PANDAS
    # ==========================================================

    dataFrame = pd.DataFrame({

        "TVD [ft]": TVDS,

        "PH [psi]": PH_vector

    })


    # ==========================================================
    # GRÁFICO INTERACTIVO PLOTLY
    # ==========================================================

    fig = go.Figure()


    # ----------------------------------------------------------
    # PH VS TVD
    # ----------------------------------------------------------

    fig.add_trace(
        go.Scatter(

            x=TVDS,

            y=PH_vector,

            mode="lines",

            name="PH vs TVD",

            line=dict(
                color="#00FF90",
                width=3.5
            )

        )
    )


    # ----------------------------------------------------------
    # PUNTO DE LA TVD INGRESADA
    # ----------------------------------------------------------

    fig.add_trace(
        go.Scatter(

            x=[TVD],

            y=[PH],

            mode="markers",

            name="Punto ingresado",

            marker=dict(
                color="red",
                size=12
            )

        )
    )


    # ----------------------------------------------------------
    # PRESIÓN DE FORMACIÓN
    # ----------------------------------------------------------

    fig.add_hline(

        y=p_formacion,

        line_dash="dash",

        annotation_text="Pform",

        annotation_position="top right"

    )


    # ==========================================================
    # CONFIGURACIÓN DEL GRÁFICO
    # ==========================================================

    fig.update_layout(

        title="Presión Hidrostática vs TVD",

        xaxis_title="TVD [ft]",

        yaxis_title="Presión Hidrostática PH [psi]",

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
        "📋 Ver datos de PH vs TVD"
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
            "### Gradiente hidrostático Gₕ"
        )

        st.latex(
            r"G_h = 0.052 \times MW"
        )


        st.write(
            "### Presión hidrostática Pₕ"
        )

        st.latex(
            r"P_h = 0.052 \times MW \times TVD"
        )


        st.write(
            "### Diferencial de presión"
        )

        st.latex(
            r"\Delta P = P_h - P_{form}"
        )


# ==============================================================
# EJECUTAR PÁGINA
# ==============================================================

show()
