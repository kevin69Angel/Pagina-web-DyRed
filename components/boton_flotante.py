import streamlit as st

def Boton_flotante():
    st.markdown("""
<style>
.boton-Glosario {
    position: fixed;
    bottom: 20px;
    right: 30px;
    background-color: white;
    color: red !important;
    padding: 10px 20px;
    border-radius: 25px;
    text-decoration: none !important;
    font-weight: bold;
    transition: background-color 0.3s ease;
    z-index: 9999;
}
.boton-Glosario:hover {
    background-color: #701705;
    text-decoration: none;
    color: white !important;
}
</style>

<a href="http://localhost:8501/Glosario" target="_self" class="boton-Glosario" aria-label="Ir al Glosario">Ir al Glosario</a>
""", unsafe_allow_html=True)