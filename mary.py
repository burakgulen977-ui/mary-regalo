import streamlit as st
from datetime import datetime

# Sayfa yapılandırması (Tarayıcı başlığı ve kalp ikonu)
st.set_page_config(page_title="Para mi Mary", page_icon="🌹", layout="centered")

# --- CUSTOM CSS (Elegant Stil) ---
st.markdown("""
    <style>
    /* Ana Arka Plan */
    .stApp {
        background: linear-gradient(to bottom, #fffcf9, #f7ede2);
    }

    /* Başlık Fontu */
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&display=swap');

    .main-title {
        font-family: 'Dancing Script', cursive;
        color: #9d0208;
        text-align: center;
        font-size: 65px;
        margin-top: -50px;
        padding-bottom: 20px;
    }

    /* Sayaç Kutusu */
    .counter-box {
        background-color: rgba(255, 255, 255, 0.6);
        padding: 20px;
        border-radius: 20px;
        border: 1px solid #e0b1cb;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SAYAÇ HESAPLAMA ---
# 10 Temmuz 2026 hedefi
target = datetime(2026, 7, 10, 0, 0, 0)
diff = target - datetime.now()
d, h, m = diff.days, diff.seconds // 3600, (diff.seconds // 60) % 60

# --- EKRAN İÇERİĞİ ---

# Elegant Başlık
st.markdown("<h1 class='main-title'>Todo vale la pena por Mary</h1>", unsafe_allow_html=True)

# Geri Sayım Kutusu
st.markdown(f"""
<div class="counter-box">
    <p style="color: #6d597a; font-size: 18px; letter-spacing: 2px; text-transform: uppercase;">Nuestro próximo encuentro</p>
    <h2 style="color: #b56576; font-size: 40px; margin: 10px 0;">{d}d : {h}h : {m}m</h2>
    <p style="color: #b56576; font-style: italic;">Cada segundo cuenta hasta volver a verte...</p>
</div>
""", unsafe_allow_html=True)

# --- MÜZİK ---
st.markdown("<h3 style='color: #31572c; text-align: center;'>🎵 Nuestra Melodía</h3>", unsafe_allow_html=True)
# Müzik dosyanın adı GitHub'a yüklerken bu olmalı
music_path = "ROMANTIC SPANISH GUITAR MUSIC. Armik, Cartas de Amor [rQKCiuSR2F8].mp3"

try:
    with open(music_path, "rb") as f:
        st.audio(f.read(), format='audio/mp3')
except:
    st.write("<p style='text-align:center; color:gray;'>Cargando música...</p>", unsafe_allow_html=True)

st.divider()

# --- HİKAYE BUTONU (GOLDEN STYLE) ---
st.markdown("### 📖 Nuestra Historia Inolvidable")
st.write(
    "He preparado algo especial para ti. Como nuestra historia es tan grande, haz clic en el botón de abajo para sumergirte en nuestros recuerdos.")

# Senin verdiğin Drive Linki
drive_url = "https://drive.google.com/file/d/1rJppOnXlgdOsJLS6Rxj81t2pZs1fD6jT/view?usp=sharing"

# Elegant bir buton tasarımı
st.link_button("✨ Abrir Nuestro Libro de Amor", drive_url, use_container_width=True)

# --- ALT NOT ---
st.write("")
st.write("")
st.markdown(
    "<p style='text-align: center; color: #6d597a; font-size: 12px;'>Creado con amor eterno para Mary • 14 de Febrero</p>",
    unsafe_allow_html=True)

# Efektler
st.balloons()