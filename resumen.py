import streamlit as st  # Importa Streamlit para mostrar datos y utilizar caché.
import pandas as pd  # Importa Pandas para crear datos tabulares de referencia.
@st.cache_data  # Guarda el resultado de la función para evitar reconstruir los datos en cada rerun.
def tabla_referencia():  # Define una función que prepara una tabla sencilla de referencia.
    return pd.DataFrame({"SG": [0.80, 0.85, 0.90], "API": [45.38, 34.97, 25.72]})  # Devuelve datos de ejemplo que serán almacenados en caché.
st.title("Resumen")  # Muestra el título de la página final.
st.write("SG actual:", st.session_state.get("sg", "Sin dato"))  # Recupera y muestra la gravedad específica guardada entre páginas.
st.write("API calculado:", st.session_state.get("api", "Todavía no calculado"))  # Recupera el resultado API si ya fue calculado.
st.dataframe(tabla_referencia(), use_container_width=True)  # Presenta la tabla de referencia reutilizando los datos en caché.
if st.button("Volver a calcular"):  # Comprueba si el usuario desea regresar a la calculadora.
    st.switch_page("api.py")  # Cambia programáticamente de vuelta hacia la calculadora.
