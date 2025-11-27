import streamlit as st
import pandas as pd
from components.boton_flotante import Boton_flotante


st.markdown(
    """
    <div style="text-align: center; padding: 5px;center;">
        <h1 style="text-align: center;margin-bottom: 20px;color:#701705; font-size: 55px;">Discución y análisis</h1>
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <div style="text-align: left; padding: 5px;margin-bottom: -30px;">
        <h3 style="margen-bottom:-50px : text-align: center">Hallazgos Principales:</h3>
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <div style="text-align: left; margin-top: 15px; margin-bottom: -5px;">
        <p>El robot concentra mayor fuerza en las <strong>patas traseras</strong> (≈70–85 N), especialmente la derecha, indicando que la **tracción principal** proviene de la parte posterior.  
    Las <strong>patas delanteras</strong> (≈15–35 N) actúan más en <strong>dirección y estabilización.</strong></p>
    </div>
    """, unsafe_allow_html=True
)



#Fuerzas
st.markdown(
    """
    <div style="text-align: center;margin-bottom: 0px; margin-top: 10px;">
        <h4 style="margen-bottom:-50px : text-align: center">Fuerzas netas por terreno:</h4>
    </div>
    """,
    unsafe_allow_html=True
)

col_left, col_center, col_right = st.columns([1, 8, 1])

with col_center:
    data = {
        "Terreno": ["Arena", "Concreto", "Césped", "Mulch", "Grava", "Tierra"],
        "Fuerzas netas delanteras (N)": ["15-21", "25-35", "18-26", "17-25", "18-25", "18-26"],
        "Fuerzas netas traseras (N)": ["70-75", "72-80", "78-88", "74-82", "78-86", "76-83"],
        "Estabilidad": ["Baja", "Muy alta", "Media", "Baja - Media", "Media - Alta", "Media - Alta"]
    }

    df = pd.DataFrame(data)

    def color_estabilidad(val):
        val_lower = val.lower()
        
        if "muy alta" in val_lower:
            bg = "#23362A"
            fg = "#0FA145"
        elif "alta" in val_lower:
            bg = "#23362A"
            fg = "#0FA145"
        elif "media" in val_lower:
            bg = "#3A3423"
            fg = "#DE960F"
        elif "baja" in val_lower:
            bg = "#330000"
            fg = "#FF3037"
        else:
            bg = "white"
            fg = "black"
        return f"background-color: {bg}; color: {fg};"

    st.dataframe(
        df.style.map(color_estabilidad, subset=["Estabilidad"]),
        width="stretch",
        )






Superficies = [
    ("Arena:", 
     "Superficie blanda y poco compacta; fuerzas delanteras irregulares y dispersas, traseras elevadas (≈70–75 N). El robot redistribuye carga hacia atrás para compensar la pérdida de apoyo."),
    ("Concreto:", 
     "Terreno rígido y estable; fuerzas limpias y constantes (delanteras ≈25–35 N, traseras ≈72–80 N). Locomoción más eficiente y equilibrada."),
    ("Césped:", 
     " Superficie semiblanda; fuerzas delanteras moderadas (≈18–26 N) y traseras más altas (≈78–88 N). Buen desempeño con ligera pérdida de eficiencia por compresibilidad."),
    ("Mulch (mantillo orgánico):", 
     "Terreno fibroso e inestable; fuerzas delanteras irregulares (≈17–25 N) y traseras fluctuantes (≈74–82 N). Se presentan deslizamientos intermitentes y mayor esfuerzo de corrección."),
    ("Grava:", 
     " Terreno granular con buena fricción; fuerzas delanteras cíclicas (≈18–25 N) y traseras regulares (≈78–86 N). Buena tracción con microajustes para estabilidad."),
    ("Tierra:", 
     " Superficie semiblanda y bien compactada; fuerzas equilibradas (delanteras ≈18–26 N, traseras ≈76–83 N) y patrón estable. Ofrece equilibrio entre adherencia y absorción.")
]

for titulo, descripcion in Superficies:
    st.divider()
    col1, col2 = st.columns([2, 2.7])
    with col1:
        st.markdown(f"<h4 style='color:#A31F05;'>{titulo}</h4>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<p style='text-align: justify; margin-top:0px ; margin-bottom: -10px ; '>{descripcion}</p>", unsafe_allow_html=True)




#Fuerzas
st.markdown(
    """
    <div style="text-align: center;margin-bottom: 0px; margin-top: 150px;">
        <h4 style="margen-bottom:-50px : text-align: center">Rango (N) por pata:</h4>
    </div>
    """,
    unsafe_allow_html=True
)


col_left, col_center, col_right = st.columns([1, 6, 1])
with col_center:
    data_2 = {
        "Pata": ["Delantera izquierda", "Delantera derecha", "Trasera izquierda", "Trasera derecha"],
        "Rango (N)": ["10-50", "10-40", "10-60", "50-120"],
        "Distribución": ["Asimétrica, con pico cerca de 15 N y caída progresiva", "Pico más marcado cerca de 25 N", "Distribución más amplia, con media en torno a 25–30 N", "Pico muy alto alrededor de 75–80 N"]
    }

    df_2 = pd.DataFrame(data_2)

    st.dataframe(df_2)      


Patas = [
    ("Pata delantera izquierda:", 
     " Se deduce que es una pata que soporta fuerzas ligeras a moderadas, probablemente es la encargada de estabilizar la marcha."),
    ("Pata delantera derecha:", 
     " Apoya en la propulsión, pero tiene cargas más constantes."),
    ("Pata trasera izquierda:", 
     "  Mayor variabilidad alterna entre apoyo y empuje según el ciclo de paso."),
    ("Pata trasera derecha: ", 
     "Es la pata que ejerce la mayor fuerza, se deduce que asume gran parte del empuje o soporte del cuerpo."),
]

for titulo, descripcion in Patas:
    st.divider()
    col1,col2= st.columns([2 , 2.7])
    with col1:
        st. markdown(f"<h4 style='color:#A31F05;'>{titulo}</h4>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<p style='text-align: justify; margin-top:0px ; margin-bottom: 30px ;'>{descripcion}</p>", unsafe_allow_html=True)


st.markdown(
       """
    <p style="text-align: left; margin-top: 10px">Las fuerzas oscilan periódicamente, reflejando el ciclo de apoyo y balanceo de cada pata. El patrón de oscilaciones es estable y repetitivo, lo que indica que la locomoción está bien sincronizada. Se aprecian picos simultáneos entre patas opuestas (delantera izquierda y trasera derecha; delantera derecha y trasera izquierda), lo cual es típico del patrón de trote en cuadrúpedos.</p>
    <p>En cuanto a la correlación o compensación de las patas se pudo evidenciar lo siguiente, entre la pata delantera izquierda y la pata trasera derecha se observa una correlación temporal en los picos de fuerza, por lo que hay un patrón diagonal de apoyo (marcha tipo trote), es decir estas dos patas son las encargadas de guiar y propulsar el movimiento y se compensan entre sí, donde la pata trasera derecha mantiene niveles altos durante casi todo el ciclo, lo que quiere decir que es el soporte dominante del mecanismo, lo que también puede significar que exista una posible asimetría mecánica o diferencia en calibración de motores, por otro lado, la pata delantera izquierda tiene picos menos pronunciados, por lo que se asume que es la pata estabilizadora que absorbe irregularidades del terreno. Mientras que la pareja diagonal de la pata delantera derecha y la para trasera izquierda no tienen una acción dominante si no que complementan el ciclo de movimiento guiadas por el otro par diagonal de patas ya explicado</p>
    <p>Con esta información se puede asumir que el robot usa un patrón de marcha estable tipo trote con alternancia diagonal, lo cual maximiza la estabilidad dinámica y la eficiencia energética.</p>
   """,
    unsafe_allow_html=True
)


Boton_flotante()