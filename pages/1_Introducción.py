import streamlit as st
# Introduccion

st.markdown(
"""
    <div style="text-align: left; padding: 5px;">
    <h1 style="text-align: center;color:#701705;margin-bottom: 20px">Introducción y planteamiento del problema</h1>
    </div>
    """, unsafe_allow_html=True
)

col1, col2 = st.columns([1, 2])
with col1:
    st.image("C:/Users/PC/Proyecto_Pagina_Web/Multipagina_Grupo_1/imagen/OIP.png",caption="DyRET Legged Robot Terrain",use_container_width=True)

with col2:
    st.markdown(
    """
    <div style="text-align: left; padding: 5px;">
        <h4>Contexto:</h4>
        <p style="font-size:16px; margin-top: 8px;">
                 Los robots cuadrúpedos bioinspirados representan un campo de rápido desarrollo en la robótica, especialmente por su capacidad para adaptarse a terrenos complejos y realizar tareas en ambientes desafiantes.
        </p>
        <p style="font-size:16px; margin-top: 8px;">El robot cuenta con dos sensores avanzados que permiten la medición precisa de fuerzas, velocidades angulares, aceleraciones lineales y orientación. Entre ellos se encuentra el sensor RAW, un dispositivo de tres ejes (Optoforce OMD-20-SH-80N) montado en el extremo de cada una de las cuatro patas, encargado de registrar las fuerzas en los ejes X, Y y Z durante el contacto con el suelo. El otro sensor que se incorpora es una unidad de medición inercial (IMU Xsens MTI-30) que integra un giroscopio de tres ejes para medir velocidades de rotación, un acelerómetro de tres ejes para registrar aceleraciones lineales y un magnetómetro de tres ejes que proporciona la orientación absoluta con respecto al campo magnético terrestre.</p>        
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
"""
<div style="text-align: left; padding: 5px;">    
    <h4>Importancia:</h4>
    <p style=" font-size:15px;">
    Este análisis contribuye al desarrollo de robots más eficientes y adaptativos, capaces de desplazarse en entornos irregulares, lo cual tiene aplicaciones en:
    </p>
    <ul>
        <li>Exploración de terrenos difíciles (energías renovables, minería, agricultura de precisión).</li>
        <li>Inspección de infraestructuras en zonas de difícil acceso.</li>
        <li>Avances en inteligencia artificial aplicada al control de movimiento.</li>
    <p style=" font-size:15px;">
    Desde la perspectiva de las TIC, este proyecto fomenta el uso de análisis de datos, machine learning y sensórica avanzada para mejorar sistemas robóticos, alineándose con los objetivos de innovación tecnológica y transformación productiva.
    </p>
    <p style=" font-size:15px;">
    Este análisis no solo contribuye a optimizar el desempeño del robot mediante la identificación de patrones en las fuerzas y movimientos, sino que también aporta al campo de la robótica aplicada y la inteligencia artificial, al generar información útil para el diseño de algoritmos de control adaptativo. En un contexto más amplio, este tipo de investigaciones apoya el desarrollo de tecnologías innovadoras y sostenibles, esenciales para la automatización de tareas en sectores industriales, agrícolas y ambientales.
    </p>
    </ul>
    <h4>Problema específico identificado</h4>
        <p>En el desarrollo tecnológico de dispositivos automatizados, uno de los desafíos actuales es mejorar la eficiencia y adaptabilidad de los robots móviles en entornos reales. En este caso, no se conoce con claridad cómo varía la distribución de las fuerzas de contacto del robot en función de la superficie y la velocidad de desplazamiento. Esta falta de información limita la posibilidad de diseñar algoritmos de control más eficientes y adaptativos o entender qué fallas se deben corregir.</p>
</div>
""",
unsafe_allow_html=True
)


st.divider()

st.markdown(
"""
<div style="text-align: center; padding: 25px;">    
    <h4>Preguntas de investigación</h4>
    <p>¿Cómo varía la fuerza ejercida por las patas del robot en relación del tipo de superficie y la velocidad de desplazamiento?</p>
</div>
""",
unsafe_allow_html=True
)

