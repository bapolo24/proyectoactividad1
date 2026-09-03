import streamlit.components.v1 as components


# ==========================================================
# COMPONENTE INTERACTIVO CON JAVASCRIPT
# ==========================================================

def componente_javascript():

    components.html(
        """
        <!DOCTYPE html>

        <html>

        <head>

            <style>

                body {

                    margin: 0;

                    padding: 0;

                    background: transparent;

                    font-family:
                        Arial,
                        Helvetica,
                        sans-serif;

                    color: #1F2937;

                }


                .panel {

                    background:
                        linear-gradient(
                            135deg,
                            #D1D5DB,
                            #E5E7EB
                        );

                    border:
                        1px solid #9CA3AF;

                    border-radius:
                        14px;

                    padding:
                        22px;

                    text-align:
                        center;

                    box-shadow:
                        0px 5px 14px
                        rgba(
                            0,
                            0,
                            0,
                            0.15
                        );

                }


                .titulo {

                    color: #1F2937;

                    font-size: 20px;

                    font-weight: bold;

                    margin-bottom: 8px;

                }


                .descripcion {

                    color: #4B5563;

                    font-size: 14px;

                    margin-bottom: 18px;

                }


                button {

                    background-color: #4B5563;

                    color: white;

                    border: none;

                    border-radius: 8px;

                    padding:
                        11px 22px;

                    font-size: 14px;

                    font-weight: bold;

                    cursor: pointer;

                    transition:
                        all 0.25s ease;

                }


                button:hover {

                    background-color: #374151;

                    transform:
                        scale(1.05);

                }


                #mensaje {

                    margin-top: 18px;

                    color: #1F2937;

                    font-size: 15px;

                    line-height: 1.8;

                    font-weight: 600;

                }

            </style>

        </head>


        <body>

            <div class="panel">

                <div class="titulo">

                    ⚙️ Verificación de Módulos Oil & Gas

                </div>


                <div class="descripcion">

                    Presione el botón para verificar
                    los módulos técnicos disponibles.

                </div>


                <button
                    onclick="verificarModulos()"
                >

                    Verificar módulos

                </button>


                <div id="mensaje">

                    Sistema listo para verificación.

                </div>

            </div>


            <script>

                function verificarModulos() {

                    const mensaje =
                        document.getElementById(
                            "mensaje"
                        );


                    mensaje.innerHTML =
                        "✅ Producción: IPR Compuesta"
                        + "<br>"
                        + "✅ Perforación: Presión Hidrostática"
                        + "<br>"
                        + "✅ Reservorios: Estimación del POES"
                        + "<br><br>"
                        + "🛢️ Todos los módulos están disponibles.";

                }

            </script>

        </body>

        </html>
        """,

        height=270
    )
