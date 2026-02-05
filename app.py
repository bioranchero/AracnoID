import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd

# 1. Configuración de seguridad
password_correcta = "aracno2026"

# Usamos la barra lateral para que no estorbe en el diseño principal
st.sidebar.title("Seguridad")
acceso = st.sidebar.text_input("Introduce la contraseña:", type="password")

if acceso == password_correcta:
    st.sidebar.success("Acceso concedido ✅")
  
else:
    if acceso == "":
        st.warning("🔒 Contraseña requerida")
        st.info("Ingresa la clave en la barra lateral para acceder a la base de datos.")
    else:
        st.error("❌ Contraseña incorrecta")
    
    # ESTA LÍNEA ES LA MÁS IMPORTANTE:
    st.stop() 

    
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

# 1. Definir las pestañas en la parte superior
tab_app, tab_registro, tab_sobre, tab_contacto = st.tabs(["🕷️ Identificador", "📝 Registrar", "👨‍🔬 Sobre Mí", "📧 Contacto"])

with tab_registro: # <--- Aquí es donde daba el error
    st.header("Reporta tu Hallazgo")
    st.write("Usa este formulario oficial para subir tus datos.")
    
    # Insertar el Google Form (Iframe)
    # Copia el link de 'Insertar' de tu Google Form
    link_google_form = "https://docs.google.com/forms/d/e/1FAIpQLSfHzqHdiPBuMuCbPYQLda8Snhp2t_V0CBURI8L8d5t-2ZdoIA/viewform?embedded=true"
    st.components.v1.iframe(link_google_form, height=900, scrolling=True)

with tab_sobre:
    st.header("Sobre el Proyecto y Autor")
    st.markdown("""
    ¡Hola! Soy Aaron, un estudiante de **Biología** apasionado por la aracnología y la tecnología aplicada a la naturaleza.
    
    **AracnoID** nació con el objetivo de:
    * Mapear la biodiversidad de arácnidos en la región de Baja California.
    * Educar a la comunidad para evitar la muerte innecesaria de especies inofensivas.
    * Proporcionar una herramienta de respuesta rápida ante especies de importancia médica.
    """)
    # Puedes añadir una foto tuya aquí si quieres
    # st.image("tu_foto.jpg", width=200)

with tab_contacto:
    st.header("📬 Contacto")
    st.write("Si tienes dudas, quieres colaborar con fotos o reportar un error, puedes encontrarme en:")
    
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.write("### Redes Sociales")
        st.write("[TikTok](https://www.tiktok.com/bioranchero)")
        st.write("[YouTube](https://www.youtube.com/bioranchero)")
    
    with col_c2:
        st.write("### Colaboración Académica")
        st.write("Si eres investigador o institución, envíame un mensaje para acceder a la base de datos completa de avistamientos.")

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

with tab_id:
# --- SECCIÓN DE IDENTIFICACIÓN ---
st.header("🔍 Identificador Rápido")
st.write("Responde según lo que observes en el ejemplar:")

# 1. La pregunta "broma" o filtro inicial
patas = st.radio("Para empezar, ¿tiene ocho patas?", ("No", "Sí"))

if patas == "No":
    st.info("¡Entonces no es una araña! 🕷️ Tal vez sea un insecto.")
else:
    # --- A PARTIR DE AQUÍ, TODO LLEVA 4 ESPACIOS DE SANGRÍA ---
    st.success("¡Perfecto! Iniciemos el registro científico. 🔬")
    
    # 1. Pregunta de los ojos
    ojos = st.radio(
        "1. ¿Cómo son los ojos de la araña?",
        ("No puedo verlos bien / Son pequeños", 
         "Tiene dos ojos centrales MUY grandes (como faros)", 
         "Tiene dos ojos grandes arriba y cuatro pequeños abajo en fila")
    )
    # ESTOS 'IF' AHORA ESTÁN DENTRO DEL 'ELSE' (con sangría extra)
    if ojos == "Tiene dos ojos centrales MUY grandes (como faros)":
        st.success("### Familia: Salticidae (Arañas Saltarinas)")
        st.write("Son inofensivas y excelentes controladoras de plagas.")
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Salticidae_eyes.jpg/320px-Salticidae_eyes.jpg")

    elif ojos == "Tiene dos ojos grandes arriba y cuatro pequeños abajo en fila":
        st.success("### Familia: Lycosidae (Arañas Lobo)")
        st.write("Suelen estar en el suelo; su veneno no es de importancia médica.")
        st.image("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgATtVEMeXZa0J-5sgTIyI5wMswVEbBY2G9C4vZ0DAHM1NuHvwQqov9Hp07WloxygvOq3Axj4OUhc39A2B5ajYNZjbvA-Pd2dUQJXJvJP57Bms4GcHj7SCyzK3sBLs1VWomSXpOZaDpyAdK/s1600/ara%C3%B1a-lobo-1.jpg")
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
url = f'https://docs.google.com/spreadsheets/d/1a0LgcfeQZiRqMBG0Rv5pi0B62XTaH-ySOJP_3Ikwzzg/export?format=csv'

st.write("---")
st.header("🗺️ Mapa de Avistamientos (Tiempo Real)")
st.info("Los colores de los pines coinciden con nuestro semáforo de riesgo biológico.")

# --- INICIO DEL BLOQUE DEL MAPA (CORREGIDO) ---
try:
    # 1. Carga de datos
    df = pd.read_csv(url)
    m = folium.Map(location=[31.8663, -116.6679], zoom_start=11)
    puntos_registro = folium.FeatureGroup(name="Avistamientos")

    # 2. Ciclo de registros
    for i, row in df.iterrows():
        riesgo_v = str(row['riesgo']).strip()
      # Definir color e icono según el riesgo
        if riesgo_v == "Peligro":
            color_f = 'red'
            icon_f = 'skull'
        elif riesgo_v == "Precaución":
            color_f = 'orange'
            icon_f = 'warning'
        else:
            color_f = 'green'
            icon_f = 'heart' # O 'microscope' para tu perfil de biología

        # El marcador con la lógica aplicada
        folium.Marker(
            location=[row['lat'], row['lon']],
            popup=f"<b>{row['especie']}</b><br>Riesgo: {riesgo_v}",
            icon=folium.Icon(color=color_f, icon=icon_f, prefix='fa')
        ).add_to(puntos_registro)

    # 3. Estas líneas van AFUERA del for (alineadas con la palabra 'for')
    puntos_registro.add_to(m)
    st_folium(m, width=700, height=450)

# 4. El except DEBE estar alineado con el 'try' inicial
except Exception as e:
    st.warning("Sincronizando base de datos local...")

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
