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

# 1. Definir las pestañas primero
tab_app, tab_sobre, tab_contacto = st.tabs(["🕷️ Identificador", "👨‍🔬 Sobre Mí", "📧 Contacto"])

# --- CONTENIDO DE LA PESTAÑA PRINCIPAL ---
with tab_app:
    st.title("🕷️ AracnoID")
    st.subheader("Guía interactiva de aracnofauna local")
    
    # MOVER AQUÍ: Todo el código del Identificador Rápido
    st.header("🔍 Identificador Rápido")
    # ... aquí van tus radios de ojos, formas, etc.
    
    # MOVER AQUÍ: Mapa y Semáforo
    st.write("---")
    # ... código del mapa y semáforo

# --- CONTENIDO DE SOBRE MÍ ---
with tab_sobre:
    st.header("Sobre el Proyecto y Autor")
    st.write("Soy un estudiante de Biología apasionado por la tecnología.")
    # El identificador NO aparecerá aquí porque está en el bloque de arriba

# --- CONTENIDO DE CONTACTO ---
with tab_contacto:
    st.header("📬 Contacto")
    # Aquí solo pones tus redes y formularios de contacto

# --- BARRA LATERAL (Monetización y Info) ---
st.sidebar.header("Sobre el Proyecto")
st.sidebar.info("""
Este proyecto es desarrollado por un estudiante de **Biología**. 
Mi meta es mapear la biodiversidad de Ensenada y educar sobre su importancia.
""")

st.sidebar.divider()
st.sidebar.write("### ☕ Apoya mi investigación")
st.sidebar.write("Si esta herramienta te fue útil, puedes apoyar el mantenimiento del servidor y mis salidas a campo.")
if st.sidebar.button("PayPal"):
    st.sidebar.write("🔗 [Haz clic aquí para donar](https://paypal.me/aaronmendezr)") # Aquí pondrás tu link real

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
            # NUEVA PREGUNTA DE COLOR
            color_viuda = st.radio("4. ¿De qué color es el cuerpo principalmente?", ("Negro brillante", "Café o pardo con dibujos"))
            
            if color_viuda == "Negro brillante":
                st.error("### Género: **Latrodectus** (Viuda Negra)")
                st.warning("⚠️ **IMPORTANCIA MÉDICA:** Su veneno es neurotóxico. No manipular y acudir al médico en caso de mordedura.")
                st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Latrodectus_hesperus_01.jpg/320px-Latrodectus_hesperus_01.jpg", caption="Latrodectus hesperus (Viuda Negra del Oeste)")
            else:
                st.warning("### Género: **Latrodectus** (Viuda Café)")
                st.write("**Descripción:** Es una especie introducida muy común en zonas urbanas de Ensenada. Aunque es de importancia médica, suele ser menos defensiva que la negra.")
                st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Latrodectus_geometricus_area.jpg/320px-Latrodectus_geometricus_area.jpg", caption="Latrodectus geometricus (Viuda Café)")
        
        else:
            st.success("### Género: **Steatoda** (Falsa Viuda)")
            st.write("**Descripción:** Muy comunes en casas. Se parecen a la viuda negra pero carecen del reloj de arena rojo.")
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
st.header("🗺️ Mapa de Avistamientos (Tiempo Real)")
st.info("Los colores de los pines coinciden con nuestro semáforo de riesgo biológico.")

# --- MAPA QUE ACUMULA TODOS LOS REGISTROS ---
try:
    df = pd.read_csv(url)

    # Creamos el mapa centrado en Ensenada
    m = folium.Map(location=[31.8663, -116.6679], zoom_start=11)
    
    # Creamos un grupo para meter todos los puntos
    puntos_registro = folium.FeatureGroup(name="Avistamientos")

    for i, row in df.iterrows():
        # Lógica de colores del semáforo
        riesgo_valor = str(row['riesgo']).strip()
        
        if riesgo_valor == "Peligro":
            color_f = 'red'; icon_f = 'skull'; pref = 'fa'
        elif riesgo_valor == "Precaución":
            color_f = 'orange'; icon_f = 'warning'; pref = 'fa'
        else:
            color_f = 'green'; icon_f = 'heart'; pref = 'glyphicon'
        
        # Añadimos cada marcador al grupo
        folium.Marker(
            location=[row['lat'], row['lon']],
            popup=f"<b>{row['especie']}</b><br>Nivel: {riesgo_valor}",
            icon=folium.Icon(color=color_f, icon=icon_f, prefix=pref),
            tooltip=f"Ver {row['especie']}"
        ).add_to(puntos_registro)

    # Agregamos el grupo completo al mapa
    puntos_registro.add_to(m)

    # Mostramos el mapa
    st_folium(m, width=700, height=450)

except Exception as e:
    st.warning("Sincronizando base de datos...")

# --- BOTÓN DE REGISTRO PARA CIENCIA CIUDADANA ---
st.write("### 📢 ¿Encontraste un ejemplar?")
st.write("Tu contribución es vital para el mapeo de la biodiversidad en Ensenada.")

# Reemplaza el link entre comillas por el enlace de tu Google Form (el que dice "Enviar")
st.link_button("➕ Registrar nuevo avistamiento", "https://docs.google.com/forms/d/e/1FAIpQLSfHzqHdiPBuMuCbPYQLda8Snhp2t_V0CBURI8L8d5t-2ZdoIA/viewform?usp=dialog")
    

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

st.write("---")
st.header("🏥 Directorio de Emergencia (Ensenada)")
st.warning("En caso de mordedura por una especie de **Importancia Médica**, acude de inmediato a estos centros. No esperes a que aparezcan los síntomas.")

col_hosp1, col_hosp2 = st.columns(2)

with col_hosp1:
    st.markdown("""
    **Hospital General de Ensenada** 📍 Av. Carretera Transpeninsular km 111  
    📞 (646) 176-7600  
    *Cuenta con antídotos (faboterápicos) para Viuda Negra y Violinista.*
    """)

with col_hosp2:
    st.markdown("""
    **IMSS Hospital General de Zona No. 8** 📍 Av. Reforma y Calle 11  
    📞 (646) 172-4500  
    *Servicio de urgencias disponible para derechohabientes.*
    """)

with st.expander("🚑 Otras unidades de apoyo"):
    st.write("""
    - **Cruz Roja Ensenada (Calle Moderna):** (646) 174-4585
    - **ISSSTE Ensenada (Calle Cuarta):** (646) 178-3511
    - **Número de Emergencia Nacional:** 911
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
