import streamlit as st

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)


st.set_page_config(page_title="Plania | Guía Docente IA", layout="centered")

# Título principal
st.title("¡Descarga GRATIS tu guía docente!")
st.subheader("5 herramientas de inteligencia artificial para planificar clases más fácil y rápido")

# Subtítulo
st.write("Esta guía express te mostrará cómo usar IA sin complicaciones para que planifiques en minutos y enseñes con más libertad.")

# Formulario
with st.form(key="formulario_guia"):
    nombre = st.text_input("Nombre")
    correo = st.text_input("Correo electrónico")
    whatsapp = st.text_input("WhatsApp (opcional)")
    submit_button = st.form_submit_button("Quiero la Guía")

# Si se envía el formulario
if submit_button:
    if nombre and correo:
        # Simula envío de email o descarga
        with open("guia_docente.pdf", "rb") as file:
            st.download_button(
                label="📥 Descargar Guía",
                data=file,
                file_name="guia_docente.pdf",
                mime="application/pdf"
            )
        st.success(f"¡Gracias {nombre} por descargar la guía!")
        st.markdown("🎉 Bienvenido/a, **profesor del futuro**. Esperamos que esta guía transforme tu forma de planificar.")
    else:
        st.warning("Por favor, completa al menos tu nombre y correo.")

# Sección extra
st.markdown("---")
st.subheader("¿Qué encontrarás en esta guía?")
st.markdown("""
✅ Las 5 mejores herramientas IA para educación  
⏳ Cómo ahorrar tiempo sin perder calidad  
⚡ Trucos rápidos para docentes ocupados  
💡 Recomendaciones prácticas con ejemplos
""")

