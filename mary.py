import streamlit as st
from datetime import datetime
import os

# Sayfa yapılandırması
st.set_page_config(page_title="Para mi Mary", page_icon="🌹", layout="centered")

# --- CUSTOM CSS (Zarif ve Elegant Stil) ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom, #fffcf9, #f7ede2);
    }
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&display=swap');
    
    .main-title {
        font-family: 'Dancing Script', cursive;
        color: #9d0208;
        text-align: center;
        font-size: 60px;
        margin-top: -30px;
        padding-bottom: 10px;
    }
    
    .counter-box {
        background-color: rgba(255, 255, 255, 0.7);
        padding: 25px;
        border-radius: 20px;
        border: 1px solid #e0b1cb;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 30px;
    }

    /* Buton stili */
    div.stButton > button {
        background-color: #9d0208 !important;
        color: white !important;
        border-radius: 20px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SAYAÇ HESAPLAMA (10 Temmuz 2026 - İlk Buluşma) ---
target = datetime(2026, 7, 10, 0, 0, 0)
diff = target - datetime.now()
d, h, m = diff.days, diff.seconds // 3600, (diff.seconds // 60) % 60

# --- EKRAN İÇERİĞİ ---

# Başlık
st.markdown("<h1 class='main-title'>Todo vale la pena por Mary</h1>", unsafe_allow_html=True)

# Geri Sayım Kutusu (İlk Görüşme Odaklı)
st.markdown(f"""
<div class="counter-box">
    <p style="color: #6d597a; font-size: 16px; letter-spacing: 2px; text-transform: uppercase; font-weight: bold;">
        Cuenta regresiva para vernos por primera vez
    </p>
    <h2 style="color: #b56576; font-size: 45px; margin: 10px 0;">{d}d : {h}h : {m}m</h2>
    <p style="color: #b56576; font-style: italic; font-size: 18px;">
        Cada segundo nos acerca al momento en que finalmente estaremos juntos... ❤️
    </p>
</div>
""", unsafe_allow_html=True)

# --- MÜZİK BÖLÜMÜ ---
st.markdown("<h3 style='color: #31572c; text-align: center; font-size: 20px;'>🎵 Nuestra Melodía</h3>", unsafe_allow_html=True)

# Müzik dosyasının GitHub'daki tam adı (Lütfen dosya adının birebir aynı olduğundan emin ol)
music_filename = "ROMANTIC SPANISH GUITAR MUSIC. Armik, Cartas de Amor [rQKCiuSR2F8].mp3"

if os.path.exists(music_filename):
    with open(music_filename, "rb") as f:
        st.audio(f.read(), format='audio/mp3')
else:
    st.write("<p style='text-align:center; color:gray;'>Haz clic para escuchar nuestra canción...</p>", unsafe_allow_html=True)

st.divider()

# --- HİKAYE BÖLÜMÜ (Drive Linki) ---
st.markdown("<h3 style='color: #9d0208;'>📖 Nuestra Historia Inolvidable</h3>", unsafe_allow_html=True)
st.write("""
He preparado algo especial para ti. Como nuestra historia es tan grande y hermosa, 
haz clic en el botón de abajo para descargar nuestro libro de amor.
""")

# Google Drive Linkin (view?usp=sharing olarak güncellendi)
drive_url = "https://drive.google.com/file/d/1rJppOnXlgdOsJLS6Rxj81t2pZs1fD6jT/view?usp=sharing"

# Elegant Buton
st.link_button("✨ Descargar Nuestro Libro de Amor (PDF)", drive_url, use_container_width=True)

st.info("Nota: Como el archivo es grande, Google te pedirá que lo descargues para verlo en alta calidad.")

# --- KÜÇÜK SÜRPRİZ ---
st.write("")
if st.button("¡Haz clic para una sorpresa extra!"):
    st.balloons()
    st.snow()
    st.toast("¡Te amo, Mary!")

# Alt Not
st.markdown("<p style='text-align: center; color: #6d597a; font-size: 13px; margin-top: 50px;'>Con todo mi amor para Mary • 14 de Febrero</p>", unsafe_allow_html=True)
