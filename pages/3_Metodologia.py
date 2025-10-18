import streamlit as st
from components.star_github import footer_component

# Metodología
st.markdown(
    """
    <div style="text-align: left; padding: 5px;">
        <h1 style="margin-bottom: 20px;color:#701705;text-align: center; font-size: 55px;">Metodología</h1>
        <h4>Diseño de la investigación:</h4>
        <p style="font-size:16px; margin-bottom: -0px;">
            <p>El presente proyecto se desarrolló bajo un diseño de investigación aplicada y descriptiva, con enfoque cuantitativo, orientado al análisis, interpretación y visualización de datos provenientes de un conjunto de información (dataset) seleccionado de acuerdo con la temática del curso.</p>
            <p>El propósito principal fue extraer conocimientos relevantes a partir de datos reales mediante técnicas de análisis y minería de datos, el proceso metodológico se estructuró en las siguientes etapas:</p>
                """,
    unsafe_allow_html=True
)


col1, col2 = st.columns(2)
with col1:
    st.markdown(
    """ 
        <ol start="1" style="font-size:16px; text-align: justify; line-height: 1.5; margin-right: 50px;margin-bottom: 40px"> 
            <li><strong>Búsqueda y selección del dataset:</strong></li>
                <p style="margin-left: 22px;">Se identificó y seleccionó una fuente de datos pertinente al tema de estudio, asegurando su calidad y disponibilidad para el análisis.</p>
            <li><strong>Análisis inicial del tema y exploración de los datos:</strong></li>
                <p style="margin-left: 22px;">Se realizó una comprensión general y una exploración preliminar de las variables contenidas en el dataset, con el fin de reconocer patrones, valores faltantes y posibles relaciones.</p>
            <li><strong>Organización y limpieza de los datos:</strong></li>    
                <p style="margin-left: 22px;">Se aplicaron procesos de depuración, transformación y normalización de la información, eliminando registros duplicados, corrigiendo inconsistencias y estandarizando formatos tanto fechas, textos y valores numericos.</p>
        """,
    unsafe_allow_html=True
)

with col2:
    st.markdown(
    """   
        <ol start="4" style="font-size:16px; text-align: justify; line-height: 1.5;margin-right: 50px;">               
            <li><strong>Minería y análisis de datos:</strong></li>
                <p style="margin-left: 22px;">Se implementaron técnicas estadísticas y de análisis para identificar tendencias, correlaciones y comportamientos significativos dentro del conjunto de datos.</p>
            <li><strong>Visualización y graficación:</strong></li>
                <p style="margin-left: 22px;">A través de herramientas de análisis de datos se generaron gráficos e indicadores visuales que facilitaron la interpretación de los resultados obtenidos.</p>
            <li><strong>Conclusiones y recomendaciones:</strong></li> 
                <p style="margin-left: 22px;">Con base en el análisis realizado, se establecieron conclusiones que resumen los hallazgos más relevantes y se formularon recomendaciones.</p>
        </ol>
    """,
    unsafe_allow_html=True
)



st.markdown(
    """
     <p>En conjunto, este diseño permitió desarrollar un proceso integral de análisis de datos, desde la adquisición hasta la interpretación final, aplicando las buenas prácticas de la analítica y fortaleciendo las competencias en el uso de herramientas tecnológicas y metodológicas del análisis de información.</p>    
        <h4>Fuentes de datos:</h4>
        <p>Los datos utilizados en este proyecto provienen del conjunto de datos público “DyRET Hexapod Locomotion Data”, disponible en el portal de acceso abierto del <strong>Commonwealth Scientific and Industrial Research Organisation (CSIRO)</strong> de Australia.</p>
        <p>Este dataset recopila información experimental obtenida a partir de las pruebas realizadas al robot DyRET (Dynamic Robot for Embodied Testing).</p>
        <h4>Técnicas de análisis utilizadas:</h4>
        <p>Se utilizaron técnicas estadísticas descriptivas, análisis de correlación, comparación de variables y visualización de datos para identificar patrones, tendencias y relaciones significativas en el conjunto de datos.</p>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
        <h4>Herramientas tecnológicas:</h4>
        <ul>
            <li>Python</li>
            <li>Seaborn</li>
            <li>Pandas</li>
            <li>Matplotlib.pyplot</li>    
            <li>Streamlit</li>
            <li>Folium</li>
            <li>Streamlit.components.v1</li>
        </ul>
    """,
    unsafe_allow_html=True
)

footer_component()