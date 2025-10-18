import streamlit as st
import folium
#TITULO PRINCIPAL
st.markdown(
    """
    <div style="text-align: center; padding: 5px; ">
        <h1 style="color:#701705;margin-top: -5px;font-size: 55px;font-weight: bold">DyRET Legged Robot Terrain Classification Dataset</h1>
        <p style="font-size:16px; margin-top: 10px;">
            <b>Fuente:</b> QCAT de CSIRO
        </p>
        <p style=" font-size:15px;">
            <b>Fecha de publicación:</b> 20 de diciembre de 2020 &nbsp;|&nbsp; <i>No ha tenido actualización</i>
        </p>
        <hr style="width:60%; margin: 20px auto;">
        <p style="text-align: justify; max-width: 700px; margin: 0 auto; font-size:16px">
            <b>Tema:</b> Recopilación de mediciones en diferentes superficies en Brisbane, Australia,
            durante noviembre de 2019, usando dos tipos de sensores del robot cuadrúpedo <b>DyRET</b>,
            sobre <b>6 superficies</b> y a <b>6 velocidades</b> diferentes.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

#Boton con link
st.markdown(
    """
    <div style="text-align: center;">
        <a href="https://www.google.com/url?q=https%3A%2F%2Fdata.csiro.au%2Fcollection%2Fcsiro%3A46885" target="_blank">
            <button style="
                background-color:#701705;
                color:white;
                border:none;
                padding:10px 20px;
                border-radius:8px;
                cursor:pointer;
                font-size:16px;
            ">
                Ir a la fuente de datos
            </button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
st.write("")




#Mapa australia
ciudad = 'Brisbane'
latitud = -31.6167
longitud = 134.3667
mapa = folium.Map(location=[latitud, longitud], zoom_start=4.4,min_zoom=4, max_zoom=18)

lat=-27.4698
log=153.0251
folium.Marker(
    location=[lat, log],
    popup=f'Marcador en {ciudad}',
    tooltip='Haz clic aquí'
).add_to(mapa)
map_html = mapa._repr_html_()
st.components.v1.html(map_html, height=500)



#Descripcón del proyecto
st.markdown("""
<div style="
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 40px;
    margin-top: 25px">
    <div style="flex:1;text-align:justify;"
        <p><strong style="font-size: 25px">🦾 Sensores</strong></p>
        <ul>
        <li style="margin-bottom:5px;">Raw: Sensor de 3 ejes en cada pata (Optoforce OMD-20-SH-80N).</li>
        <li style="margin-bottom:30px;">IMU: Giroscopio, acelerómetro y magnetómetro de 3 ejes (Xsens MTI-30).</li>
        </ul>
        <p><strong style="font-size: 25px">🔬 Uso del dataset</strong></p>
        <ul>
        <li style="margin-bottom:5px;">Validación de modelos cinemáticos/dinámicos.</li>  
        <li style="margin-bottom:30px;">Clasificación de terreno mediante señales de contacto.</li>
        <ul>
        <p><strong style="font-size: 25px">⚙ Velocidades y pasos</strong></p>
        <ul>
        <li>Velocidades: 0–1: 0.125 Hz, 2–3: 0.1875 Hz, 4–5: 0.25 Hz.</li>
        </ul>
        <ul>
        <li style="margin-top:-11px;">Longitudes de paso: 0, 2, 4 → 80 mm; 1, 3, 5 → 120 mm. </li> 
        </ul>
    </div>
    <div style="flex:1;text-align:justify;"
        <p><strong style="font-size: 25px">🧩 Metadatos</strong></p>
        <ul>
        <li style="margin-bottom:5px;">Licencia: Creative Commons 4.0</li>  
        <li style="margin-bottom:5px;">Actualizaciones: No.</li>  
        <li style="margin-bottom:30px;">Recolección: 10 pruebas por archivo, 8 pasos cada una, en todas las </li>
        </ul>
        <p style="margin-top:-35px;">superficies y velocidades (total: 2880 pasos).</p> 
        <p><strong style="font-size: 25px; margin-bottom: 50px">🌍 Superficies</strong></p>
        <p style="margin-bottom:30px;">Hormigón, césped, grava, mulch, tierra, arena.</p>
        <p><strong style="font-size: 25px">🎯 Propósito</strong></p>
        <p style="margin-bottom:30px;">Evaluar el rendimiento del robot DyRET según la fuerza aplicada por cada pata</p>
        <p style="margin-top:-35px;">durante la marcha.</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.divider()

col1, col2 = st.columns([1, 2])

with col1:
    st.image("C:/Users/PC/Proyecto_Pagina_Web/Multipagina_Grupo_1/imagen/descarga (1).png",caption="Ejes x y z",)

with col2:
    st.markdown(
    """
    <div style="text-align: left; padding: 5px;">
        <h4>ejes</h4>
        <p style="font-size:16px; margin-top: 8px;">
                 Los robots cuadrúpedos bioinspirados representan un campo de rápido desarrollo en la robótica, especialmente por su capacidad para adaptarse a terrenos complejos y realizar tareas en ambientes desafiantes.
        </p>
        <p style="font-size:16px; margin-top: 8px;">Uno de ellos es el sensor RAW, instalado en el extremo de cada una de sus cuatro patas. Este sensor puede detectar las fuerzas que actúan en tres direcciones, llamadas ejes X, Y y Z:</p> 
    <ul>
    <li>El eje X mide los movimientos hacia adelante y hacia atrás.</li>
    <li>El eje Y mide los desplazamientos hacia los lados.</li>
    <li>El eje Z mide las fuerzas verticales, es decir, hacia arriba y hacia abajo.</li>
    </ul>
    <p style="font-size:16px; margin-top: 8px;">Gracias a esta información, el robot puede saber cuánta presión ejerce cada pata al tocar el suelo, lo que mejora su equilibrio y estabilidad al caminar.</p> 

    </div>
    """,
    unsafe_allow_html=True
)

#Hito 2
st.markdown(
    """
    <div style="text-align: center; padding: 5px; margin-top: 70px; ">
        <h1 style="color:#701705;margin-top: -5px;">Exploración Inicial de Datos en Python</h1>
        <p style="font-size:16px; margin-top: 10px;">
        <hr style="width:60%; margin: 20px auto;">
        <p style="text-align: center; max-width: 700px; margin: 0 auto; font-size:16px">
            <b>Esta fase se centra en asegurar la calidad de su dataset y en realizar un análisis exploratorio exhaustivo (EDA) para descubrir patrones, 
            anomalías y relaciones iniciales entre las variables.<b>DyRET</b>,
            sobre <b>6 superficies</b> y a <b>6 velocidades</b> diferentes.
        <div style=" justify-content: center; gap: 15px;margin-top: 30px">
        <a href="https://colab.research.google.com/drive/1uczDqJNx-5RfNXIooJ5xJSgQ4Cw2fzrs" target="_blank">
            <button style="
                background-color:#701705;
                color:white;
                border:none;
                padding:10px 20px;
                border-radius:8px;
                cursor:pointer;
                font-size:16px;
            ">
               ¡Haz clik!
            </button>
        </a>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

#hito 3
st.markdown(
    """
    <div style="text-align: center; padding: 5px; margin-top: 50px; ">
        <h1 style="color:#701705;margin-top: -5px;">Limpieza y Exploración de Datos con Pandas</h1>
        <p style="font-size:16px; margin-top: 10px;">
        <hr style="width:60%; margin: 20px auto;">
        <p style="text-align: center; max-width: 700px; margin: 0 auto; font-size:16px">
            <b>El objetivo de esta fase es realizar un "chequeo médico" a su dataset. Necesitamos entender su estructura,
             identificar los tipos de variables y detectar posibles problemas (como datos faltantes) desde el principio.<b>DyRET</b>,
            sobre <b>6 superficies</b> y a <b>6 velocidades</b> diferentes.
        <div style=" justify-content: center; gap: 15px;margin-top: 30px">
        </a>
                <a href="https://colab.research.google.com/drive/1qRZ1FP8FBRl9PFz39juQCs_E4Itvn2lQ" target="_blank">
            <button style="
                background-color:#701705;
                color:white;
                border:none;
                padding:10px 20px;
                border-radius:8px;
                cursor:pointer;
                font-size:16px;
            ">
                ¡Haz clik!
            </button>
        </a>   
    </div>
    """,
    unsafe_allow_html=True
)

st.link_button("Glosario","http://localhost:8501/Glosario")