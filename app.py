import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Aracno-Ensenada | Biología",
    page_icon="🕷️",
    layout="centered"
)

# Estilos personalizados para que se vea más profesional
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #2e7d32;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Título Principal
st.title("🕷️ Aracno-Ensenada")
st.subheader("Guía interactiva de aracnofauna local")
st.write("Herramienta desarrollada para el estudio y divulgación de los arácnidos en Baja California.")

# --- BARRA LATERAL (Monetización y Info) ---
st.sidebar.header("Sobre el Proyecto")
st.sidebar.info("""
Este proyecto es desarrollado por un estudiante de **Biología**. 
Mi meta es mapear la biodiversidad de Ensenada y educar sobre su importancia.
""")

st.sidebar.divider()
st.sidebar.write("### ☕ Apoya mi investigación")
st.sidebar.write("Si esta herramienta te fue útil, puedes apoyar el mantenimiento del servidor y mis salidas a campo.")
if st.sidebar.button("Invítame un café (PayPal)"):
    st.sidebar.write("🔗 [Haz clic aquí para donar](https://www.paypal.com)") # Aquí pondrás tu link real

st.sidebar.divider()
st.sidebar.write("### 📢 ¡Sígueme!")
st.sidebar.write("[TikTok](https://www.tiktok.com) | [YouTube](https://www.youtube.com)")

# --- SECCIÓN DE IDENTIFICACIÓN ---
st.header("🔍 Identificador Rápido")
st.write("Responde según lo que observes en el ejemplar:")

# Pregunta 1: Los ojos (Base científica)
ojos = st.radio(
    "1. ¿Cómo son los ojos de la araña?",
    ("No puedo verlos bien / Son pequeños", 
     "Tiene dos ojos centrales MUY grandes (como faros)", 
     "Tiene dos ojos grandes arriba y cuatro pequeños abajo en fila")
)

if ojos == "Tiene dos ojos centrales MUY grandes (como faros)":
    st.success("### Familia: **Salticidae** (Arañas Saltarinas)")
    st.write("**Descripción:** Son arañas cazadoras activas con excelente visión. Son totalmente inofensivas para los humanos y ayudan a controlar plagas.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Salticidae_eyes.jpg/320px-Salticidae_eyes.jpg", caption="Patrón ocular típico de Salticidae")

elif ojos == "Tiene dos ojos grandes arriba y cuatro pequeños abajo en fila":
    st.success("### Familia: **Lycosidae** (Arañas Lobo)")
    st.write("**Descripción:** No tejen telas circulares, suelen estar en el suelo. Aunque impresionan por su tamaño, su veneno no es de importancia médica.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Wolf_spider_eyes.jpg/320px-Wolf_spider_eyes.jpg", caption="Patrón ocular típico de Lycosidae")

else:
    # Pregunta 2: Morfología
    forma = st.radio(
        "2. ¿Qué forma tiene el cuerpo?",
        ("Globoso (como una canica o uva)", 
         "Aplanado con una marca oscura en el frente", 
         "Alargado u otro")
    )

    if forma == "Globoso (como una canica o uva)":
        mancha = st.radio("3. ¿Tiene una mancha roja o naranja brillante en el vientre?", ("No", "Sí"))
        
        if mancha == "Sí":
            st.error("### Género: **Latrodectus** (Viuda Negra)")
            st.warning("⚠️ **IMPORTANCIA MÉDICA:** Su veneno es neurotóxico. No manipular y acudir al médico en caso de mordedura.")
        else:
            st.success("### Género: **Steatoda** (Falsa Viuda)")
            st.write("**Descripción:** Muy comunes en casas de Ensenada. Se parecen a la viuda negra pero carecen del reloj de arena rojo. Su mordedura es similar a una picadura de avispa.")

    elif forma == "Aplanado con una marca oscura en el frente":
        violin = st.radio("3. ¿Ves una mancha clara en forma de violín en el cefalotórax?", ("No estoy seguro", "Sí, se ve clara"))
        
        if violin == "Sí, se ve clara":
            st.error("### Género: **Loxosceles** (Araña Violinista)")
            st.warning("⚠️ **IMPORTANCIA MÉDICA:** Su veneno es necrótico. Es una araña tímida pero peligrosa.")
        else:
            st.info("Podría ser una araña de la familia Filistatidae o similar. Toma una foto para identificación avanzada.")

# --- SECCIÓN DE PRIMEROS AUXILIOS ---
st.divider()
with st.expander("🆘 ¿Qué hacer en caso de mordedura? (Primeros Auxilios)"):
    st.markdown("""
    1. **Mantén la calma:** Evita que el veneno se distribuya rápido.
    2. **Lava la zona:** Usa agua limpia y jabón.
    3. **Aplica frío:** Una compresa fría ayudará con el dolor y la inflamación.
    4. **Fotografía al ejemplar:** Es crucial para que el médico sepa qué antídoto aplicar.
    5. **NO SUCCIONES ni hagas cortes.** Son mitos que empeoran la herida.
    
    *En Ensenada, acude al Hospital General o al centro de salud más cercano si presentas síntomas graves.*
    """)

# Pie de página
st.write("---")
st.caption("© 2026 Aracno-Ensenada. Proyecto educativo de Biología.")
