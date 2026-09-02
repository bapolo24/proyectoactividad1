import streamlit as st  # Importa Streamlit para controlar la navegación general de la aplicación.
inicio = st.Page("inicio.py", title="Home", icon="🏠", default=True)  # Define la página principal y la establece como predeterminada.
Produccion = st.Page("produccion.py", title="Calculadora API", icon="🛢️")  # Define la página destinada al cálculo del grado API.
Perforacion = st.Page("perforacion.py", title="Resumen", icon="📊")  # Define una página adicional para visualizar datos precargados.
Rerservorios = st.Page("reservorios.py", title="Resumen", icon="📊")  # Define una página adicional para visualizar datos precargados.
paginas = {"Principal": [inicio], "Ejercicios": [Produccion, Perforacion, Reservorios]}  # Agrupa las páginas en secciones dentro de la navegación.
pagina = st.navigation(paginas)  # Construye el menú multipágina utilizando los grupos definidos.
pagina.run()  # Ejecuta solamente la página elegida por el usuario.
