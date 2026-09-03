import streamlit as st


def cargar_estilos():

    st.html(
        """
        <style>

        /* =====================================================
           FONDO GENERAL
        ===================================================== */

        .stApp {

            background:
                linear-gradient(
                    135deg,
                    #E5E7EB 0%,
                    #D6DAE0 50%,
                    #CBD1D8 100%
                );

        }


        /* =====================================================
           CONTENEDOR PRINCIPAL
        ===================================================== */

        [data-testid="stMainBlockContainer"] {

            padding-top: 2rem;

            padding-bottom: 3rem;

        }


        /* =====================================================
           TIPOGRAFÍA
        ===================================================== */

        html,
        body {

            font-family:
                Arial,
                Helvetica,
                sans-serif;

        }


        h1 {

            color: #1F2937 !important;

            font-weight: 750 !important;

        }


        h2 {

            color: #273549 !important;

            font-weight: 700 !important;

        }


        h3 {

            color: #374151 !important;

        }


        /* =====================================================
           TEXTO GENERAL
        ===================================================== */

        [data-testid="stMarkdownContainer"] p {

            color: #374151;

        }


        /* =====================================================
           LABEL DE LOS INPUTS
        ===================================================== */

        [data-testid="stWidgetLabel"] p {

            color: #1F2937 !important;

            font-weight: 650 !important;

        }


        /* =====================================================
           NUMBER INPUT
        ===================================================== */

        [data-testid="stNumberInput"] input {

            background-color:
                #FFFFFF !important;

            color:
                #111827 !important;

            border:
                1px solid #9CA3AF !important;

            border-radius:
                8px !important;

            font-weight:
                600;

        }


        /* =====================================================
           EXPANDERS
        ===================================================== */

        [data-testid="stExpander"] {

            background-color:
                #F3F4F6;

            border:
                1px solid #AEB5BE;

            border-radius:
                12px;

            box-shadow:
                0 3px 10px
                rgba(
                    0,
                    0,
                    0,
                    0.10
                );

            margin-bottom:
                16px;

        }


        /* =====================================================
           TARJETA RESULTADOS
        ===================================================== */

        .oil-card {

            background:
                linear-gradient(
                    145deg,
                    #4B5563,
                    #374151
                );

            border:
                1px solid #6B7280;

            border-radius:
                16px;

            min-height:
                165px;

            padding:
                22px 18px;

            margin:
                5px 0px 12px 0px;

            text-align:
                center;

            display:
                flex;

            flex-direction:
                column;

            align-items:
                center;

            justify-content:
                center;

            box-shadow:
                0px 6px 16px
                rgba(
                    0,
                    0,
                    0,
                    0.20
                );

            transition:
                transform 0.25s ease,
                box-shadow 0.25s ease;

        }


        .oil-card:hover {

            transform:
                translateY(-4px);

            box-shadow:
                0px 11px 25px
                rgba(
                    0,
                    0,
                    0,
                    0.28
                );

        }


        .oil-card-icon {

            font-size:
                32px;

            margin-bottom:
                7px;

        }


        .oil-card-title {

            color:
                #D1D5DB;

            font-size:
                15px;

            font-weight:
                650;

            margin-bottom:
                5px;

        }


        .oil-card-value {

            color:
                #FFFFFF;

            font-size:
                29px;

            font-weight:
                750;

            margin-bottom:
                4px;

        }


        .oil-card-unit {

            color:
                #FBBF24;

            font-size:
                14px;

            font-weight:
                650;

        }


        /* =====================================================
           TARJETAS HOME
        ===================================================== */

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
                16px;

            padding:
                24px 20px;

            min-height:
                245px;

            text-align:
                center;

            display:
                flex;

            flex-direction:
                column;

            align-items:
                center;

            justify-content:
                center;

            box-shadow:
                0px 5px 14px
                rgba(
                    0,
                    0,
                    0,
                    0.13
                );

            transition:
                transform 0.25s ease,
                box-shadow 0.25s ease;

        }


        .home-card:hover {

            transform:
                translateY(-5px);

            box-shadow:
                0px 10px 24px
                rgba(
                    0,
                    0,
                    0,
                    0.19
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
                15px;

        }


        .home-card-text {

            color:
                #4B5563;

            font-size:
                14px;

            line-height:
                1.55;

        }


        .home-card-separator {

            width:
                50px;

            border-top:
                2px solid #9CA3AF;

            margin:
                15px auto;

        }


        .home-card-subtitle {

            color:
                #374151;

            font-size:
                13px;

            font-weight:
                700;

            margin-bottom:
                4px;

        }


        .home-card-model {

            color:
                #1F2937;

            font-size:
                14px;

            font-weight:
                600;

        }


        /* =====================================================
           TARJETAS DE TECNOLOGÍA
        ===================================================== */

        .tech-card {

            background-color:
                #F8FAFC;

            border:
                1px solid #AEB5BE;

            border-radius:
                14px;

            padding:
                20px 12px;

            min-height:
                155px;

            display:
                flex;

            flex-direction:
                column;

            align-items:
                center;

            justify-content:
                center;

            text-align:
                center;

            box-shadow:
                0px 4px 12px
                rgba(
                    0,
                    0,
                    0,
                    0.11
                );

        }


        .tech-icon {

            font-size:
                30px;

            margin-bottom:
                8px;

        }


        .tech-title {

            color:
                #1F2937;

            font-size:
                17px;

            font-weight:
                750;

            margin-bottom:
                8px;

        }


        .tech-text {

            color:
                #4B5563;

            font-size:
                13px;

            line-height:
                1.45;

        }


        /* =====================================================
           BLOQUE INFORMATIVO
        ===================================================== */

        .technical-info {

            background-color:
                #F3F4F6;

            color:
                #1F2937;

            border-left:
                5px solid #4B5563;

            border-radius:
                10px;

            padding:
                18px 20px;

            margin:
                15px 0px 22px 0px;

            box-shadow:
                0px 4px 11px
                rgba(
                    0,
                    0,
                    0,
                    0.10
                );

        }


        .technical-info-title {

            color:
                #1F2937;

            font-size:
                17px;

            font-weight:
                750;

            margin-bottom:
                8px;

        }


        .technical-info-text {

            color:
                #4B5563;

            line-height:
                1.55;

        }


        /* =====================================================
           FOOTER
        ===================================================== */

        .footer-oil {

            background-color:
                #F3F4F6;

            border:
                1px solid #B8BEC6;

            border-radius:
                12px;

            padding:
                20px;

            text-align:
                center;

            color:
                #374151;

        }


        .footer-title {

            color:
                #1F2937;

            font-weight:
                750;

            font-size:
                16px;

            margin-bottom:
                8px;

        }


        .footer-text {

            color:
                #4B5563;

            font-size:
                13px;

            margin-top:
                3px;

        }


        /* =====================================================
           TABS
        ===================================================== */

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


        /* =====================================================
           SIDEBAR
        ===================================================== */

        section[data-testid="stSidebar"] {

            background-color:
                #E5E7EB;

        }


        section[data-testid="stSidebar"] * {

            color:
                #1F2937;

        }


        /* =====================================================
           ALERTAS
        ===================================================== */

        [data-testid="stAlert"] {

            border-radius:
                10px;

        }

        </style>
        """
    )
