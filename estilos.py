import streamlit as st


def cargar_estilos():

    st.markdown(
        """
<style>

/* =========================================================
   FONDO GENERAL DE LA APLICACIÓN
========================================================= */

.stApp {
    background: linear-gradient(
        135deg,
        #E5E7EB 0%,
        #D1D5DB 50%,
        #CBD5E1 100%
    );
}


/* =========================================================
   CONTENIDO PRINCIPAL
========================================================= */

[data-testid="stMainBlockContainer"] {
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* =========================================================
   TEXTO GENERAL
========================================================= */

html,
body,
p,
span,
label,
div {
    font-family: Arial, Helvetica, sans-serif;
}


/* =========================================================
   TÍTULOS
========================================================= */

h1 {
    color: #1F2937 !important;
    font-weight: 750 !important;
}

h2 {
    color: #263238 !important;
    font-weight: 700 !important;
}

h3 {
    color: #374151 !important;
    font-weight: 650 !important;
}


/* =========================================================
   TEXTO NORMAL STREAMLIT
========================================================= */

[data-testid="stMarkdownContainer"] p {
    color: #374151;
}


/* =========================================================
   LABELS DE NUMBER INPUT
========================================================= */

[data-testid="stWidgetLabel"] p {
    color: #1F2937 !important;
    font-weight: 600 !important;
}


/* =========================================================
   CAMPOS NUMBER INPUT
========================================================= */

[data-testid="stNumberInput"] input {

    background-color: #F8FAFC !important;

    color: #111827 !important;

    border:
        1px solid #9CA3AF !important;

    border-radius: 8px !important;
}


/* =========================================================
   EXPANDERS
========================================================= */

[data-testid="stExpander"] {

    background-color: #F3F4F6;

    border:
        1px solid #9CA3AF;

    border-radius: 12px;

    margin-bottom: 15px;

    box-shadow:
        0 3px 8px
        rgba(0, 0, 0, 0.10);
}


[data-testid="stExpander"] summary {

    color: #1F2937 !important;

    font-weight: 650 !important;
}


/* =========================================================
   TARJETAS DE RESULTADOS
========================================================= */

.oil-card {

    background:
        linear-gradient(
            145deg,
            #4B5563,
            #374151
        );

    border:
        1px solid #6B7280;

    border-radius: 16px;

    padding: 22px 18px;

    margin:
        8px 0px 14px 0px;

    text-align: center;

    min-height: 165px;

    display: flex;

    flex-direction: column;

    justify-content: center;

    box-shadow:
        0px 6px 15px
        rgba(
            0,
            0,
            0,
            0.18
        );

    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease;
}


.oil-card:hover {

    transform:
        translateY(-4px);

    box-shadow:
        0px 10px 24px
        rgba(
            0,
            0,
            0,
            0.26
        );
}


/* =========================================================
   ÍCONO DE LA TARJETA
========================================================= */

.oil-card-icon {

    font-size: 31px;

    margin-bottom: 8px;
}


/* =========================================================
   TÍTULO DE LA TARJETA
========================================================= */

.oil-card-title {

    color: #E5E7EB;

    font-size: 15px;

    font-weight: 600;

    margin-bottom: 8px;
}


/* =========================================================
   VALOR PRINCIPAL
========================================================= */

.oil-card-value {

    color: #FFFFFF;

    font-size: 29px;

    font-weight: 750;

    margin-bottom: 6px;
}


/* =========================================================
   UNIDAD
========================================================= */

.oil-card-unit {

    color: #FBBF24;

    font-size: 14px;

    font-weight: 600;
}


/* =========================================================
   BLOQUE INFORMATIVO
========================================================= */

.technical-info {

    background:
        #F3F4F6;

    color:
        #1F2937;

    border-left:
        5px solid #4B5563;

    padding:
        18px 20px;

    border-radius:
        10px;

    margin:
        15px 0px 22px 0px;

    box-shadow:
        0px 4px 10px
        rgba(
            0,
            0,
            0,
            0.10
        );
}


/* =========================================================
   TARJETAS HOME
========================================================= */

.home-card {

    background:
        linear-gradient(
            145deg,
            #F9FAFB,
            #E5E7EB
        );

    border:
        1px solid #9CA3AF;

    border-radius:
        15px;

    padding:
        24px;

    min-height:
        220px;

    text-align:
        center;

    box-shadow:
        0px 5px 14px
        rgba(
            0,
            0,
            0,
            0.12
        );

    transition:
        0.25s ease;
}


.home-card:hover {

    transform:
        translateY(-4px);

    box-shadow:
        0px 10px 22px
        rgba(
            0,
            0,
            0,
            0.18
        );
}


.home-card-icon {

    font-size:
        40px;

    margin-bottom:
        10px;
}


.home-card-title {

    color:
        #1F2937;

    font-size:
        20px;

    font-weight:
        750;

    margin-bottom:
        10px;
}


.home-card-text {

    color:
        #4B5563;

    font-size:
        14px;

    line-height:
        1.5;
}


/* =========================================================
   TABS
========================================================= */

button[data-baseweb="tab"] {

    color:
        #374151 !important;

    font-size:
        16px;

    font-weight:
        650;
}


button[data-baseweb="tab"][aria-selected="true"] {

    color:
        #111827 !important;
}


/* =========================================================
   SIDEBAR
========================================================= */

section[data-testid="stSidebar"] {

    background:
        #D1D5DB;
}


section[data-testid="stSidebar"] * {

    color:
        #1F2937;
}


/* =========================================================
   DATAFRAME
========================================================= */

[data-testid="stDataFrame"] {

    border-radius:
        10px;

    overflow:
        hidden;
}


/* =========================================================
   CAPTION
========================================================= */

[data-testid="stCaptionContainer"] {

    color:
        #4B5563 !important;
}


/* =========================================================
   INFO / SUCCESS / WARNING / ERROR
========================================================= */

[data-testid="stAlert"] {

    border-radius:
        10px;
}

</style>
        """,
        unsafe_allow_html=True
    )
