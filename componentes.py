import streamlit as st


def cargar_estilos():

    st.markdown(
        """
        <style>

        /* =========================================
           FONDO GENERAL
        ========================================= */

        .stApp {

            background:
                linear-gradient(
                    135deg,
                    #07111f 0%,
                    #0b1f33 50%,
                    #102a43 100%
                );

        }


        /* =========================================
           TÍTULOS
        ========================================= */

        h1, h2, h3 {

            font-family:
                Arial,
                Helvetica,
                sans-serif;

        }


        /* =========================================
           TARJETAS OIL & GAS
        ========================================= */

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
                    0.10
                );

            border-radius: 16px;

            padding: 22px;

            margin: 8px 0px;

            text-align: center;

            box-shadow:
                0px 6px 18px
                rgba(
                    0,
                    0,
                    0,
                    0.25
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
                    0.35
                );

        }


        .oil-card-icon {

            font-size: 30px;

        }


        .oil-card-title {

            color: #b8c7d9;

            font-size: 15px;

            margin-top: 7px;

        }


        .oil-card-value {

            color: #ffffff;

            font-size: 28px;

            font-weight: 700;

            margin-top: 5px;

        }


        .oil-card-unit {

            color: #f4b942;

            font-size: 13px;

        }


        /* =========================================
           BLOQUE INFORMATIVO
        ========================================= */

        .technical-info {

            background:
                rgba(
                    15,
                    42,
                    67,
                    0.85
                );

            border-left:
                5px solid #f4b942;

            padding: 16px;

            border-radius: 8px;

            margin:
                15px 0px;

        }

        </style>
        """,

        unsafe_allow_html=True
    )
