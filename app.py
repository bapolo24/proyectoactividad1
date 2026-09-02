import streamlit as st  # Importa Streamlit para controlar la navegación general de la aplicación.
inicio = st.Page("inicio.py", title="Home", icon="🏠", default=True)  # Define la página principal y la establece como predeterminada.
Produccion = st.Page("produccion.py", title="Produccion", icon="🛢️")  # Define la página destinada al cálculo del grado API.
Perforacion = st.Page("perforacion.py", title="Perforacion", icon="🏗️")  # Define una página adicional para visualizar datos precargados.
Reservorios = st.Page("reservorios.py", title="Reservorios", icon="🌍")  # Define una página adicional para visualizar datos precargados.
paginas = {"Principal": [inicio], "Ejercicios": [Produccion, Perforacion, Reservorios]}  # Agrupa las páginas en secciones dentro de la navegación.
pagina = st.navigation(paginas)  # Construye el menú multipágina utilizando los grupos definidos.
pagina.run()  # Ejecuta solamente la página elegida por el usuario.
