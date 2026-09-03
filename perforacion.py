import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go


def show():

    st.header("🏗️ Perforacion")

    st.write(
        "Calculadora de presión hidrostática "
            )

    # ==========================================================
    # PARÁMETROS DE LA PERFORACIÓN
    # ==========================================================

    with st.sidebar.expander(
        "🛠️ Parámetros de Perforación",
        expanded=True
    ):

        p
        MW = st.number_input(
            "Peso de lodo (MW) [ppg]",
            value=20.0,
            step=1.0
        )

        MD = st.number_input(
            "Profundidad medida del pozo (MD) [ft]",
            value=20000,
            step=100
        )

        TVD = st.number_input(
            "Profundidad vertical verdadera (TVD) [ft]",
            value=500.0,
            step=10.0
        )

        p_formacion= st.number_input(
            "Presión de Formacion (Pform) [psi]",
            value=6000.0,
            step=100.0
        )


    # ==========================================================
    # VALIDACIONES
    # ==========================================================

    if TVD <= 0:
        st.error(
            "⚠️ La profundidad TVD debe ser mayor que cero."
        )
        return

    if MD <= 0:
        st.error(
            "⚠️ La profundidad MD debe ser mayor que cero."
        )
        return

    if MW <= 8:
        st.error(
            "⚠️ El peso de lodo debe ser mayor que 8"
        )
        return

    if p_formacion < 0:
        st.error(
            "⚠️ La presión de formacion no puede ser negativa."
        )
        return

    if MD >= TVD:
        st.error(
            "⚠️ Siempe el MD es mayor o igual que el TVD:"
            " MD >= TVD."
        )
        return


    # ==========================================================
    # PRESION HIDROSTATICA
    # ==========================================================

    PH = 0.052 * MW * TVD


    # ==========================================================
    # GRADIENTE HIDROSTÁTICO
    # ==========================================================

    GRAD_H = 0.052 * MW 

    # ==========================================================
    # DIFERENCIAL DE PRESIÓN
    # ==========================================================

     DIF_P= PH-p_formacion
    # ==========================================================
  
    # ==========================================================
    # RESULTADOS
   
    # ==========================================================
    # GENERACIÓN DE LA PH Vs TVD
    # ==========================================================

    # Se generan valores de presión de formación desde Pr hasta 0 psi

    PH_vector = np.linspace(
        PH,
        0,
        PH
    )

    TVD = []


   
    TVDS = np.array(TVDS)


    # ==========================================================
    # DATAFRAME CON PANDAS
    # ==========================================================

    dataFrame = pd.DataFrame({

        "PH [psi]": PH,

        "TVD [psi]": TVDS

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

            x=PH,

            y=TVDS,

            mode="lines",

            name="PH Vs TVD",

            line=dict(
                color="#00FF90",
                width=3.5
            )

        )
    )


    

    # ==========================================================
    # CONFIGURACIÓN DEL GRÁFICO
    # ==========================================================

    fig.update_layout(

        title="PH vs TVD",

        xaxis_title=(
            "PH [psi]"
        ),

        yaxis_title=(
            "TVD [ft]"
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
    # INFORMACIÓN DEL CÁLCULO
    # ==========================================================

    with st.expander(
        "🧮 Ver ecuaciones utilizadas"
    ):

        st.write(
            "### Gradiente hidrostático Gₕ"
        )

        st.latex(
            r"Gₕ = 0.052 × MW"
        )
        st.write(
            "### Presión hidrostática Pₕ"
        )

        st.latex(
            r"= 0.052 × MW × TVD"
        )
        st.write(
            "### Diferencial de presión"
        )

        st.latex(
            r"=  ΔP = Pₕ − Pform"
        )


