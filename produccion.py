import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import time

def show():
    st.header("📈 IPR ")
  
    # --- PARÁMETROS DEL RESERVORIO ---
    with st.sidebar.expander("🛠️ Parámetros del Reservorio", expanded=True):
        p_res = st.number_input("Presión de Reservorio (Pr) [psi]", value=3000, step=100)
        ip = st.number_input("Índice de Productividad (IP) [bpd/psi]", value=1.5, step=0.1)
        p_bur = st.number_input("Presión de burbuja (Pbur) [psi]", value=500, step=10)
        p_wf = st.number_input("Presión de fondo fluyente (Pwf) [psi]", value=500, step=10)
        
    # --- CÁLCULO DE IPR (OFERTA) ---
    caudal_max = ip * p_res
    # Generamos un vector denso para mayor precisión en la intersección
    caudales = np.linspace(0.1, caudal_max if caudal_max > 0 else 100.0, 200) 
    pwf = p_res - (caudales / ip)
    pwf = np.maximum(pwf, 0.0)
      # --- GRÁFICO INTERACTIVO PLOTLY ---
    fig = go.Figure()
    
    # Curva IPR
    fig.add_trace(go.Scatter(
    x=caudales, y=pwf,
    name="IPR (Oferta Yacimiento)",
    line=dict(color='#00FF90', width=3.5)
