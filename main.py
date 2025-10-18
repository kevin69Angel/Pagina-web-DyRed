import streamlit as st

st.set_page_config(
    page_title="Dashboard TTCH",
    layout="wide", 
    page_icon="📊",
    initial_sidebar_state="expanded"
)

grupo_1 = [
    st.Page("pages/Presentación.py", title="Presentación", icon="👋"),
        st.Page("pages/1_Contexto.py", title="Contexto", icon="📖"),
    st.Page("pages/1_Introducción.py", title="Introducción y plantamiento del problema", icon="🚀"),
    st.Page("pages/2_Objetivos.py", title=" Objetivo general y específicos", icon="🎯"),
    st.Page("pages/3_Metodologia.py", title="Metodología", icon="🛠️"), 
]

datasets = [
    st.Page("pages/graphics.py", title="Graficos", icon="📈"),
    st.Page("pages/Discusión_y_análisis.py", title="Discusión y análisis", icon="🔍"),
    st.Page("pages/Conclusiones y recomendaciones.py", title="Conclusiones y recomendaciones", icon="🎉"),
    st.Page("pages/Referencias_Bibliograficas.py", title="Referencias Bibliográficas", icon="📚"),
    st.Page("pages/Glosario.py", title="Glosario", icon="📕")
]

extra = [
    st.Page("pages/about.py", title="Acerca de", icon="🌐"),
    st.Page("pages/contact.py", title="Contacto", icon="📞")

]

pages = {
    "💻 Documentación": grupo_1,
    "📂 Resultados principales": datasets,
    "⚙️ Otros": extra
}

pg = st.navigation(pages)
pg.run()