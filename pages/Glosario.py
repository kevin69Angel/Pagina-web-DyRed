import streamlit as st
from components.star_github import footer_component

st.markdown(
    """
    <div style="text-align: center; padding: 5px; ">
        <h1 style="color:#701705;margin-top: -5px; font-size: 55px;">Glosario</h1>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <ul>
        <li style=" font-size:25px; margin-top: 35px;margin-bottom: -2px"><strong>Sensor RAW:</strong></p>
            <p style="font-size: 20px; margin-top: -20px;">Datos sin procesar obtenidos directamente de los sensores del robot (en este caso, mediciones de fuerza y posición).</p>
        <li style=" font-size:25px; margin-top: 35px;margin-bottom: -2px"><strong>IMU (Unidad de Medición Inercial):</strong></li>
            <p style="font-size: 20px;margin-left: 35px;">Dispositivo (Xsens MTI-30) que integra un giroscopio, un acelerómetro y un magnetómetro, permitiendo medir velocidades angulares, aceleraciones lineales y orientación respecto al campo magnético terrestre.</p>
        <li style=" font-size:25px; margin-top: 35px;margin-bottom: -2px"><strong>Fx, Fy, Fz:</strong></li>
            <p style="font-size: 20px;margin-left: 35px;"> Componentes de la fuerza medida por cada pata en los ejes X (horizontal), Y (lateral) y Z (vertical).</p>
        <li style=" font-size:25px; margin-top: 35px;margin-bottom: -2px"><strong>Velocidad de marcha:</strong></li>
            <p style="font-size: 20px;margin-left: 35px;">Frecuencia de paso o ritmo al que el robot avanza; puede estar asociada a una frecuencia en Hz.</p>
        <li style=" font-size:25px; margin-top: 35px;margin-bottom: -2px"><strong>Superficie o terreno:</strong></li>
            <p style="font-size: 20px;margin-left: 35px;">Material sobre el que se desplaza el robot (por ejemplo: arena, pasto, concreto).</p> 
        <li style=" font-size:25px; margin-top: 35px;margin-bottom: -2px"><strong>Datos atípicos (outliers):</strong></li>
            <p style="font-size: 20px;margin-left: 35px;"> Valores que se alejan considerablemente del comportamiento general de los datos, posiblemente por errores o condiciones especiales.</p> 
        <li style=" font-size:25px; margin-top: 35px;margin-bottom: -2px"><strong>Correlación:</strong></li>
            <p style="font-size: 20px;margin-left: 35px;"> Relación estadística entre dos variables que indica cómo una cambia respecto a la otra.  </p> 
        <li style=" font-size:25px; margin-top: 35px;margin-bottom: -2px"><strong>F_L:</strong></li>
            <p style="font-size: 20px;margin-left: 35px;">Pata delantera izquierda.</p>
        <li style=" font-size:25px; margin-top: 35px;margin-bottom: -2px"><strong>F_R:</strong></li>
            <p style="font-size: 20px;margin-left: 35px;">Pata delantera derecha.</p>
        <li style=" font-size:25px; margin-top: 35px;margin-bottom: -2px"><strong>B_L:</strong></li>
            <p style="font-size: 20px;margin-left: 35px;"> Pata trasera izquierda.</p>
        <li style=" font-size:25px; margin-top: 35px;margin-bottom: -2px"><strong>B_R:</strong></li>
            <p style="font-size: 20px;margin-left: 35px;"> Pata trasera derecha.</p>



    </ul>


    """,
    unsafe_allow_html=True
)










footer_component()