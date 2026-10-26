app_code = """
import streamlit as st

# Título de la aplicación
st.title("Convertidor de Texto a Mayúsculas")

# Caja de texto de entrada
texto_usuario = st.text_input("Escribe tu texto aquí:", "")

# Procesamiento y visualización
if texto_usuario:
    texto_mayusculas = texto_usuario.upper()
    st.subheader("Texto en Mayúsculas:")
    st.write(texto_mayusculas)
else:
    st.info("Por favor, escribe algo en la caja de texto para procesarlo.")
"""

with open("app.py", "w", encoding="utf-8") as f:
    f.write(app_code.strip())
