import streamlit.components.v1 as components


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

                    font-family:
                        Arial,
                        Helvetica,
                        sans-serif;

                    background:
                        transparent;

                    color:
                        white;

                    text-align:
                        center;
                }


                #panel {

                    background:
                        linear-gradient(
                            135deg,
                            #102a43,
                            #164e63
                        );

                    padding: 20px;

                    border-radius: 14px;

                    border:
                        1px solid
                        rgba(
                            255,
                            255,
                            255,
                            0.12
                        );
                }


                button {

                    background:
                        #f4b942;

                    color:
                        #07111f;

                    border:
                        none;

                    border-radius:
                        8px;

                    padding:
                        11px 20px;

                    font-size:
                        14px;

                    font-weight:
                        bold;

                    cursor:
                        pointer;

                    transition:
                        transform 0.2s ease;
                }


                button:hover {

                    transform:
                        scale(1.05);
                }


                #mensaje {

                    margin-top:
                        15px;

                    font-size:
                        15px;

                    line-height:
                        1.7;
                }

            </style>

        </head>


        <body>

            <div id="panel">

                <h3>
                    🛢️ Oil & Gas Engineering
                </h3>

                <p>
                    Verificación interactiva
                    de los módulos técnicos
                </p>

                <button
                    onclick="verificarModulos()"
                >

                    Verificar módulos

                </button>

                <div id="mensaje">

                    Presione el botón para
                    ejecutar la interacción.

                </div>

            </div>


            <script>

                function verificarModulos() {

                    const mensaje =
                        document.getElementById(
                            "mensaje"
                        );

                    mensaje.innerHTML =
                        "✅ Producción: IPR Compuesta activa"
                        + "<br>"
                        + "✅ Perforación: Presión Hidrostática activa"
                        + "<br>"
                        + "✅ Reservorios: POES activo";

                }

            </script>

        </body>

        </html>
        """,

        height=250
    )
