import streamlit as st  # Importa Streamlit para usar widgets, navegación y session_state.
st.title("Calculadora de Grado API")  # Muestra el título principal de la herramienta.
sg = st.number_input("Gravedad específica", value=st.session_state.get("sg", 0.85))  # Solicita SG utilizando como valor inicial el dato conservado en la sesión.
st.session_state.sg = sg  # Guarda el valor actual de SG para reutilizarlo en otras páginas.
if st.button("Calcular"):  # Comprueba si el usuario solicitó realizar el cálculo.
    api = (141.5 / sg) - 131.5  # Calcula el grado API con la ecuación estándar.
    st.session_state.api = api  # Guarda también el resultado API dentro de session_state.
    st.metric("Resultado", f"{api:.2f} °API")  # Presenta el resultado en un widget métrico.
if st.button("Ir al resumen"):  # Comprueba si el usuario desea continuar hacia la siguiente página.
    st.switch_page("resumen.py")  # Cambia programáticamente hacia la página de resumen.
