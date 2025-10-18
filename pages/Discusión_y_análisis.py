import streamlit as st

st.markdown(
    """
    <div style="text-align: center; padding: 5px;center;">
        <h1 style="text-align: center;margin-bottom: 20px;color:#701705; font-size: 55px;">Discución y análisis</h1>
        <h4 style="margen-bottom:-50px : text-align: center">Hallazgos Principales:</h4>
    </div>
    """,
    unsafe_allow_html=True
)


#FUERZAS POR TERRENO
col1, col2 = st.columns([1,2])
with col2:
    st.image("C:/Users/PC/Proyecto_Pagina_Web/Multipagina_Grupo_1/imagen/terreno.png", caption="Fuerzas netas por terreno",use_container_width=True)
with col1:
    st.markdown(
       """
       <ul style="text-align: justify; margin-right: 15px;">
            <p>
                El robot concentra mayor fuerza en las patas traseras (≈70–85 N), especialmente la derecha, indicando que la tracción principal proviene de la parte posterior. Las patas delanteras (≈15–35 N) actúan más en dirección y estabilización.</p>
            <li><strong>Arena:</strong> Superficie blanda y poco compacta; fuerzas delanteras irregulares y dispersas, traseras elevadas (≈70–75 N). El robot redistribuye carga hacia atrás para compensar la pérdida de apoyo.</li>
            <li><strong>Concreto:</strong> Terreno rígido y estable; fuerzas limpias y constantes (delanteras ≈25–35 N, traseras ≈72–80 N). Locomoción más eficiente y equilibrada.</li>

        </ul>
   """,
    unsafe_allow_html=True
)

st.markdown(
       """
    <ul>
        <li style="text-align: left; margin-top:  -13px;"><strong>Césped:</strong> Superficie semiblanda; fuerzas delanteras moderadas (≈18–26 N) y traseras más altas (≈78–88 N). Buen desempeño con ligera pérdida de eficiencia por compresibilidad.</li>
        <li><strong>Mulch (mantillo orgánico):</strong> Terreno fibroso e inestable; fuerzas delanteras irregulares (≈17–25 N) y traseras fluctuantes (≈74–82 N). Se presentan deslizamientos intermitentes y mayor esfuerzo de corrección.</li>
        <li><strong>Grava:</strong> Terreno granular con buena fricción; fuerzas delanteras cíclicas (≈18–25 N) y traseras regulares (≈78–86 N). Buena tracción con microajustes para estabilidad.</li>
        <li><strong>Tierra:</strong> Superficie semiblanda y bien compactada; fuerzas equilibradas (delanteras ≈18–26 N, traseras ≈76–83 N) y patrón estable. Ofrece equilibrio entre adherencia y absorción.</li>

    </ul>
   """,
    unsafe_allow_html=True
)



st.divider()

#RANGO POR PATAS

st.markdown(
    """
    <div style="text-align: left; padding: 5px;margin-top: -40px">
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns([1,2])
with col2:
    st.image("C:/Users/PC/Proyecto_Pagina_Web/Multipagina_Grupo_1/imagen/patas.png", caption="Rango por pata",use_container_width=True)
with col1:
    st.markdown(
       """
       <ul style="text-align: justify; margin-right: 15px;">
            <li><strong>Pata delantera izquierda:</strong>  Se deduce que es una pata que soporta fuerzas ligeras a moderadas, probablemente es la encargada de estabilizar la marcha.</li>
            <li><strong>Pata delantera derecha:</strong> Apoya en la propulsión, pero tiene cargas más constantes.
            <li><strong>Pata trasera izquierda:</strong> Mayor variabilidad alterna entre apoyo y empuje según el ciclo de paso.
            <li><strong>Pata trasera derecha:</strong>  Es la pata que ejerce la mayor fuerza, se deduce que asume gran parte del empuje o soporte del cuerpo.
             </li>
            <li>Las fuerzas oscilan periódicamente, reflejando el ciclo de apoyo y balanceo de cada pata. El patrón de oscilaciones es estable y repetitivo, lo que indica que la locomoción está bien
             </li>

        </ul>
   """,
    unsafe_allow_html=True
)


st.markdown(
       """
    <p style="text-align: left; margin-left: 22px;  margin-top: -15px">sincronizada. Se aprecian picos simultáneos entre patas opuestas (delantera izquierda y trasera derecha; delantera derecha y trasera izquierda), lo cual es típico del patrón de trote en cuadrúpedos.</p>
    <p style="text-align: left; margin-left: 22px;  margin-top: -15px">En cuanto a la correlación o compensación de las patas se pudo evidenciar lo siguiente, entre la pata delantera izquierda y la pata trasera derecha se observa una correlación temporal en los picos de fuerza, por lo que hay un patrón diagonal de apoyo (marcha tipo trote), es decir estas dos patas son las encargadas de guiar y propulsar el movimiento y se compensan entre sí, donde la pata trasera derecha mantiene niveles altos durante casi todo el ciclo, lo que quiere decir que es el soporte dominante del mecanismo, lo que también puede significar que exista una posible asimetría mecánica o diferencia en calibración de motores, por otro lado, la pata delantera izquierda tiene picos menos pronunciados, por lo que se asume que es la pata estabilizadora que absorbe irregularidades del terreno. Mientras que la pareja diagonal de la pata delantera derecha y la para trasera izquierda no tienen una acción dominante si no que complementan el ciclo de movimiento guiadas por el otro par diagonal de patas ya explicado</p>
    <p style="text-align: left; margin-left: 22px;  margin-top: -15px">Con esta información se puede asumir que el robot usa un patrón de marcha estable tipo trote con alternancia diagonal, lo cual maximiza la estabilidad dinámica y la eficiencia energética.</p>
   """,
    unsafe_allow_html=True
)
