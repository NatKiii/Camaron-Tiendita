import streamlit as st
import base64

def poner_musica(archivo):
    with open(archivo, "rb") as f:
        datos = f.read()
    b64 = base64.b64encode(datos).decode()
    codigo_reproductor = """
        <audio id="musica" autoplay loop>
            <source src="data:audio/mp3;base64,""" + b64 + """" type="audio/mp3">
        </audio>
        <script>
            var audio = document.getElementById("musica");
            audio.play().catch(function() {
                window.parent.document.addEventListener("click", function() {
                    audio.play();
                }, { once: true });
            });
        </script>
    """
    st.components.v1.html(codigo_reproductor, height=0)

# --- ESTILOS, FUENTES CUTES Y ALINEACIÓN (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Quicksand:wght@500;700&display=swap');

    .stApp {
        background-color: #fff0f5;
    }
    
    /* Aplicar fuente Quicksand a todo el texto general */
    html, body, [class*="st-"] {
        font-family: 'Quicksand', sans-serif;
        color: #8b4557;
    }

    /* Fuente tierna para el título principal */
    h1 {
        font-family: 'Pacifico', cursive;
        color: #d63384 !important;
        text-align: center;
        font-size: 3.5rem;
    }

    /* Centrar encabezados y textos */
    h2, h3, p {
        text-align: center;
        color: #994d62;
    }

    /* Centrar columnas y alinear elementos para que no queden chuecos */
    div[data-testid="column"] {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        justify-content: space-between;
    }

    /* Uniformizar el tamaño de las imágenes del catálogo para que queden alineadas */
    div[data-testid="column"] img {
        object-fit: cover;
        border-radius: 15px;
    }

    /* Estilizar botones para que combinen con el estilo cute */
    .stButton>button {
        background-color: #ffb6c1;
        color: white;
        border-radius: 20px;
        border: 2px solid #ff69b4;
        font-family: 'Quicksand', sans-serif;
        font-weight: bold;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #ff69b4;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# --- REPRODUCIR MÚSICA ---
poner_musica("musicapag.mp3")

# --- PÁGINA WEB ---
st.title("💖 Camarón")
st.header("Bienvenido a nuestra tienda de figuras cutes")
st.write("¡Aquí podrás encontrar las figuras más lindas de todo Chile!")

# --- FOTO PRINCIPAL Y VIDEO (CENTRADOS) ---
col_izq, col_centro, col_der = st.columns([1, 2, 1])

with col_centro:
    st.image("camaron.jpg", width=500)
    st.video("BaileCamaron.mp4", width=250)

st.markdown("---")

# --- CATÁLOGO DE PRODUCTOS (EN COLUMNAS ALINEADAS) ---
st.subheader("🛍️ Catálogo Destacado")
col1, col2, col3 = st.columns(3)

with col1:
    st.image("Focacamaron.png", caption="Figura Camarón foca - $5.000", width=180)
    if st.button("Comprar Figura", key="btn1"):
        st.balloons()
        st.success("¡Agregado al carrito! 🌸")

with col2:
    st.image("Gatocamaron.jpg", caption="Figura Camarón gato - $6.000", width=180)
    if st.button("Comprar Figura", key="btn2"):
        st.balloons()
        st.success("¡Agregado al carrito! 🎀")

with col3:
    st.image("Jacobo.jpg", caption="Figura Jacobo nuestro señor - $10.000", width=180)
    if st.button("Comprar Figura", key="btn3"):
        st.balloons()
        st.success("¡Agregado al carrito! ✨")

st.markdown("---")

# --- SECCIÓN EXTRA: BOTÓN SORPRESA ---
col_s1, col_s2, col_s3 = st.columns([1, 2, 1])
with col_s2:
    if st.button("Haz clic para una sorpresa 🐾"):
        st.image("meimei.jpg", width=500)
        st.write("¡Meimei te extraña mucho y te manda un abrazo!")

st.markdown("---")

# --- FORMULARIO DE PEDIDO ---
with st.form("formulario_pedido"):
    st.subheader("💌 ¡Haz tu encargo!")
    nombre_cliente = st.text_input("Tu nombre:")
    figura_elegida = st.selectbox("¿Qué figura deseas encargar?", ["Foca Camarón", "Gato Camarón", "Jacobo"])
    comentarios = st.text_input("Algún detalle o comuna para entrega:")
    
    enviar = st.form_submit_button("Enviar pedido")
    
    if enviar:
        if nombre_cliente:
            st.success("¡Muchas gracias " + nombre_cliente + "! Tu pedido de " + figura_elegida + " ha sido anotado con éxito 💖")
            st.balloons()
        else:
            st.warning("Por favor, ingresa tu nombre antes de enviar el pedido.")

# --- CUADRO DE TEXTO PERSONALIZADO ---
st.markdown("---")
user_input = st.text_input("Déjanos un mensajito o saludo:")
if user_input:
    st.write("Escribiste: " + user_input + " (¡Qué lindo mensaje! 💌)")