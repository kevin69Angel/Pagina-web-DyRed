import streamlit as st
from components.boton_flotante import Boton_flotante

# Objetivos
st.markdown(
    """
    <div style="text-align: center; padding: 5px;center;">
        <h1 style="text-align: center;margin-bottom: 20px;color:#701705;font-size: 55px;">Objetivos</h1>
        <h4>Objetivo general:</h4>
        <p style="font-size:16px; margin-top: 8px;">
         Analizar la relación existente entre la fuerza ejercida por las patas del robot y las características de la superficie sobre la que se desplaza, considerando las variaciones de velocidad y tipo de terreno.
        </p>
        <h4>Objetivos específicos:</h4>
        <ul>
            <li>Comparar las fuerzas realizadas por cada pata y la relación que hay entre ellas durante la marcha.</li>
            <li>Examinar el comportamiento de los componentes de la fuerza (Fx, Fy, Fz) en distintas muestras del sensor raw.</li>
            <li>Definir una hipótesis respecto a la existencia de datos atípicos.</li>    
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

Boton_flotante()