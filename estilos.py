import streamlit as st


def cargar_estilos():

    st.markdown(
        """
        <style>

        /* =====================================================
           FONDO GENERAL
        ===================================================== */

        .stApp {
            background:
                linear-gradient(
                    135deg,
                    #07111f 0%,
                    #0b1f33 50%,
                    #102a43 100%
                );
        }


        /* =====================================================
           TEXTO GENERAL
        ===================================================== */

        html, body, [class*="css"] {
            font-family:
                Arial,
                Helvetica,
                sans-serif;
        }


        /* =====================================================
           TÍTULOS
        ===================================================== */

        h1 {
            color: #ffffff;
            font-weight: 700;
        }

        h2 {
            color: #e6edf5;
            font-weight: 650;
        }

        h3 {
            color: #e6edf5;
        }


        /* =====================================================
           TARJETAS PERSONALIZADAS
        ===================================================== */

        .oil-card {

            background:
                linear-gradient(
                    145deg,
                    #102a43,
                    #163a59
                );

            border:
                1px solid rgba(
                    255,
                    255,
                    255,
                    0.12
                );

            border-radius: 16px;

            padding: 22px;

            margin-top: 8px;

            margin-bottom: 12px;

            text-align: center;

            box-shadow:
                0px 6px 18px
                rgba(
                    0,
                    0,
                    0,
                    0.30
                );

            transition:
                transform 0.25s ease,
                box-shadow 0.25s ease;
        }


        .oil-card:hover {

            transform:
                translateY(-4px);

            box-shadow:
                0px 10px 28px
                rgba(
                    0,
                    0,
                    0,
                    0.40
                );
        }


        .oil-card-icon {

            font-size: 32px;

            margin-bottom: 5px;
        }


        .oil-card-title {

            color: #b9c8d8;

            font-size: 15px;

            font-weight: 600;

            margin-bottom: 6px;
        }


        .oil-card-value {

            color: #ffffff;

            font-size: 28px;

            font-weight: 750;

            margin-bottom: 4px;
        }


        .oil-card-unit {

            color: #f4b942;

            font-size: 14px;

            font-weight: 500;
        }


        /* =====================================================
           BLOQUE TÉCNICO
        ===================================================== */

        .technical-info {

            background:
                rgba(
                    15,
                    42,
                    67,
                    0.90
                );

            border-left:
                5px solid #f4b942;

            padding: 18px;

            border-radius: 10px;

            margin-top: 15px;

            margin-bottom: 20px;

            color: #e9f1f7;

            box-shadow:
                0px 4px 12px
                rgba(
                    0,
                    0,
                    0,
                    0.20
                );
        }


        /* =====================================================
           TABS
        ===================================================== */

        button[data-baseweb="tab"] {

            font-weight: 600;

            font-size: 16px;
        }


        /* =====================================================
           BOTONES
        ===================================================== */

        div.stButton > button {

            border-radius: 10px;

            font-weight: bold;
        }


        /* =====================================================
           SIDEBAR
        ===================================================== */

        section[data-testid="stSidebar"] {

            background-color: #071522;
        }

        </style>
        """,

        unsafe_allow_html=True
    )
