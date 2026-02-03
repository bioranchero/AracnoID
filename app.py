import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd

# Configuración de la página
st.set_page_config(
    page_title="AracnoID | Biología",
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
st.title("🕷️ AracnoID")
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
    st.sidebar.write("🔗 [Haz clic aquí para donar](https://www.paypal.com/aaronmendezr)") # Aquí pondrás tu link real

st.sidebar.divider()
st.sidebar.write("### 📢 ¡Sígueme!")
st.sidebar.write("[TikTok](https://www.tiktok.com/bioranchero) | [YouTube](https://www.youtube.com/bioranchero)")

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
    st.image("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgATtVEMeXZa0J-5sgTIyI5wMswVEbBY2G9C4vZ0DAHM1NuHvwQqov9Hp07WloxygvOq3Axj4OUhc39A2B5ajYNZjbvA-Pd2dUQJXJvJP57Bms4GcHj7SCyzK3sBLs1VWomSXpOZaDpyAdK/s1600/ara%C3%B1a-lobo-1.jpg", caption="Patrón ocular típico de Lycosidae")

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

st.write("---")
st.header("🚦 Semáforo de Riesgo Arácnido")

col1, col2, col3 = st.columns(3)

with col1:
    st.error("🔴 **PELIGRO**")
    st.write("- Violinista\n- Viuda Negra")
    st.caption("Importancia médica severa.")

with col2:
    st.warning("🟡 **PRECAUCIÓN**")
    st.write("- Falsa Viuda\n- Araña de Saco")
    st.caption("Mordedura dolorosa, riesgo bajo.")

with col3:
    st.success("🟢 **ALIADAS**")
    st.write("- Saltarinas\n- Arañas Lobo")
    st.caption("Inofensivas y controlan plagas.")

# --- CONFIGURACIÓN DE DATOS ---
# Recuerda cambiar 'TU_ID_AQUÍ' por el ID de tu hoja de Google
SHEET_ID = '1a0LgcfeQZiRqMBG0Rv5pi0B62XTaH-ySOJP_3Ikwzzg'
url = f'https://docs.google.com/spreadsheets/d/1a0LgcfeQZiRqMBG0Rv5pi0B62XTaH-ySOJP_3Ikwzzg/gviz/tq?tqx=out:csv'

st.write("---")
st.header("🗺️ Mapa de Avistamientos (Sincronizado)")
st.info("Los colores de los pines coinciden con nuestro semáforo de riesgo biológico.")

try:
    df = pd.read_csv(url)

    # Centro el mapa en las coordenadas de tu primer registro en Ensenada
    m = folium.Map(location=[31.8663, -116.6679], zoom_start=12)

  # Recorremos las filas de tu Google Form
    for i, row in df.iterrows():
        # Lógica de colores y calaveras basada en tu columna 'riesgo'
        # Usamos .get() por si acaso una celda está vacía
        riesgo_valor = str(row['riesgo']).strip()
        
        if riesgo_valor == "Peligro":
            color_final = 'red'
            icono_final = 'skull'
            prefijo = 'fa'
        elif riesgo_valor == "Precaución":
            color_final = 'orange'
            icono_final = 'warning'
            prefijo = 'fa'
        else:
            color_final = 'green'
            icono_final = 'leaf'
            prefijo = 'glyphicon'
        
    folium.Marker(
            location=[row['lat'], row['lon']],
            popup=f"<b>{row['especie']}</b><br>Nivel: {riesgo_valor}",
            icon=folium.Icon(color=color_final, icon=icono_final, prefix=prefijo),
            tooltip="Click para ver detalle"
        ).add_to(m)

    st_folium(m, width=700, height=450)

except Exception as e:
    st.warning("Conectando con la base de datos de Google Sheets...")
    

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

# --- SECCIÓN DE PREGUNTAS FRECUENTES ---
st.divider()
st.header("❓ Preguntas Frecuentes")
with st.expander("¿Todas las arañas son peligrosas?"):
    st.write("""
    No. La gran mayoría de las arañas son inofensivas y juegan un papel crucial en el ecosistema controlando plagas de insectos. 
    En México, solo los géneros *Loxosceles* (violinista) y *Latrodectus* (viuda negra) son considerados de importancia médica severa.
    """)

with st.expander("¿Qué hago si encuentro una araña en mi casa?"):
    st.write("""
    Si no es de importancia médica, lo ideal es reubicarla usando un frasco y una hoja de papel. 
    Si sospechas que es peligrosa, no intentes manipularla directamente. Mantén la calma y usa esta guía para identificarla.
    """)

with st.expander("¿La app puede identificar cualquier especie del mundo?"):
    st.write("""
    Actualmente, **AracnoID** se enfoca en las familias más comunes y de importancia médica. 
    Como estudiante de biología, voy actualizando la base de datos para incluir más especies de la región de Baja California y el resto del país.
    """)

with st.expander("¿Cómo puedo colaborar con el proyecto?"):
    st.write("""
    ¡Tus avistamientos ayudan! Puedes contactarme por mis redes sociales para enviarme fotos nítidas 
    (especialmente de los ojos y marcas del cuerpo) para seguir nutriendo esta herramienta educativa.
    """)

# Pie de página
st.write("---")
st.caption("© 2026 AracnoID.")
