import streamlit.components.v1 as components


def componente_javascript():

    components.html(
        """
        <!DOCTYPE html>

        <html>

        <head>

            <style>

                body {

                    font-family:
                        Arial,
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

                    padding:
                        18px;

                    border-radius:
                        14px;

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
                        10px 18px;

                    font-weight:
                        bold;

                    cursor:
                        pointer;

                }


                button:hover {

                    transform:
                        scale(1.05);

                }


                #mensaje {

                    margin-top:
                        15px;

                    font-size:
                        16px;

                }

            </style>

        </head>


        <body>

            <div id="panel">

                <h3>
                    🛢️ Oil & Gas Engineering
                </h3>

                <button
                    onclick="mostrarEstado()"
                >

                    Verificar módulos

                </button>

                <div id="mensaje">

                    Presione el botón
                    para verificar la aplicación.

                </div>

            </div>


            <script>

                function mostrarEstado() {

                    const mensaje =
                        document.getElementById(
                            "mensaje"
                        );

                    mensaje.innerHTML =
                        "✅ Producción activa"
                        + "<br>"
                        + "✅ Perforación activa"
                        + "<br>"
                        + "✅ Reservorios activos";

                }

            </script>

        </body>

        </html>
        """,

        height=230
    )
