from components.star_github import footer_component
import streamlit as st

st.title(" Acerca de")
st.write(
    """
    Esta aplicación ha sido desarrollada con **Streamlit** como parte de un proyecto de formación
    en desarrollo Full Stack e inteligencia artificial.

    Su objetivo es ofrecer una experiencia educativa y práctica para analizar datos, construir
    interfaces web dinámicas y aplicar técnicas modernas de desarrollo.
    """
)

st.divider()

st.subheader("👨‍💻 Autores")
st.write(
    """
    **Desarrollado por:** Joan Esteban Méndez  
    **Rol:** Desarrollador Full Stack & Analista de Datos  
    **GitHub:** [joanestebandev](https://github.com/joanestebandev)
    """
)

st.write()
st.write(
    """
    **Desarrollado por:** Kevin Angel Giraldo  
    **Rol:** web developer & Analista de Datos  
    **GitHub:** [kevin69Angel](https://github.com/kevin69Angel?tab=repositories)
    """
)
st.write()
st.write(
    """
    **Desarrollado por:**  Maria Cristina Hernandez  
    **Rol:** Analista de Datos  
    """
)
st.write()
st.write(
    """
    **Desarrollado por:**  Maria Paula Iglesias  
    **Rol:** Analista de Datos  
    """
)
st.divider()

st.subheader("🛠️ Tecnologías utilizadas")
st.markdown(
    """
    - **Python** 🐍  
    - **Streamlit** para la interfaz interactiva  
    - **Pandas**, **Matplotlib** y **Scikit-learn** para el análisis de datos  
    - **Docker** para contenerización  
    - **GitHub Actions** para automatización del despliegue
    """
)

footer_component()