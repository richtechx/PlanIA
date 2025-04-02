import streamlit as st

st.set_page_config(page_title="Plania | Guía Docente IA", layout="centered")

# Estilos CSS para personalizar el diseño
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        padding: 10px 24px;
        font-size: 16px;
    }
    .stTextInput > div > input {
        border-radius: 6px;
    }
    </style>
""", unsafe_allow_html=True)

# Título principal
st.markdown("## 🎓 ¡Descarga GRATIS tu guía docente!")
st.markdown("### ⚙️ 5 herramientas de inteligencia artificial para planificar clases más fácil y rápido")

# Subtítulo
st.markdown("Esta guía express te mostrará cómo usar IA sin complicaciones para que planifiques en minutos y enseñes con más libertad. 🚀")

# Espacio
st.markdown("---")

# Formulario
with st.form(key="formulario_guia"):
    st.markdown("### 📝 Completa el formulario para recibir tu guía")
    nombre = st.text_input("👤 Nombre")
    correo = st.text_input("📧 Correo electrónico")
    whatsapp = st.text_input("📱 WhatsApp (opcional)")
    submit_button = st.form_submit_button("📘 Quiero la Guía")

# Si se envía el formulario
if submit_button:
    if nombre and correo:
        with open("guia_docente.pdf", "rb") as file:
            st.download_button(
                label="📥 Descargar Guía en PDF",
                data=file,
                file_name="guia_docente.pdf",
                mime="application/pdf"
            )
        st.success(f"✅ ¡Gracias {nombre} por descargar la guía!")
        st.markdown("🎉 Bienvenido/a, **profesor del futuro**. Tu transformación educativa comienza hoy.")
    else:
        st.warning("⚠️ Por favor, completa al menos tu nombre y correo para continuar.")

# Sección de contenido extra
st.markdown("---")
st.markdown("## 📚 ¿Qué encontrarás en esta guía?")
st.markdown("""
- 🔍 **Las 5 mejores herramientas IA para educación**  
- ⏱️ **Cómo ahorrar tiempo sin perder calidad**  
- ⚡ **Trucos rápidos para docentes ocupados**  
- 💡 **Recomendaciones prácticas con ejemplos reales**

---

📌 Ideal para docentes que quieren innovar sin complicarse.  
🧠 Diseñada con enfoque pedagógico y tecnología educativa.
""")

    
        
