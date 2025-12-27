import streamlit as st
import random
import time

# =========================
# FUNNY & TEASING WEBSITE
# =========================
st.set_page_config(
    page_title="Luvi Jangan Marah 😝",
    page_icon="😂",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- Mobile First + Fun CSS ---
st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: 'Comic Sans MS', 'Arial Rounded MT Bold', sans-serif;
}

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
    max-width: 430px;
}

h1 {
    font-size: 1.9rem !important;
    text-align: center;
    color: #ff3d3d;
}

h4 {
    font-size: 1rem !important;
    text-align: center;
    color: #444;
}

p {
    font-size: 1rem !important;
    line-height: 1.6;
}

button {
    width: 100%;
    border-radius: 30px;
    padding: 0.7rem 0;
    font-size: 1rem;
}
</style>
""", unsafe_allow_html=True)

# =========================
# CONTENT
# =========================

st.markdown("""
<h1>😂 Website Khusus Luvi 😂</h1>
<h4>Dibaca dengan senyum, bukan baper</h4>
<hr>
""", unsafe_allow_html=True)

st.markdown(
    """
    <p>
    Hai <b>Luvi Hana Margareta</b> 😌<br><br>
    Website ini dibuat dengan niat mulia:
    <b>mengejek kamu secara elegan dan penuh cinta</b> 😝<br><br>
    Kalau kamu ketawa, berarti misiku berhasil.
    Kalau kamu kesel... ya berarti kena 😌
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

st.subheader("Pilih kejujuranmu 🤔")
choice = st.radio(
    "Luvi itu orangnya gimana sih?",
    [
        "😇 Baik, tapi ngeselin",
        "😌 Ngeselin, tapi dirindukan",
        "🤡 Ngeselin dan bangga akan itu"
    ]
)

if choice:
    st.success("Jawaban diterima. Tidak bisa dibantah 😌")

st.divider()

# Roast Button
st.subheader("Tombol Rahasia (Jangan Ditekan) 🚨")

roasts = [
    "Luvi itu tipe orang yang bilang 'terserah', tapi kalau salah… kamu tetap salah 🤡",
    "Luvi kalau ngambek itu bukan marah, tapi nunggu diperhatiin 😌",
    "Luvi ngeselin bukan karena niat, tapi karena bakat 💅",
    "Kalau Luvi bilang 'aku gapapa', itu artinya kamu dalam bahaya 🚨",
    "Luvi bisa bikin orang senyum dan emosi di waktu yang sama. Talenta langka 🎭",
]

if st.button("Aku Berani Tekan 😈"):
    with st.spinner("Mengeluarkan ejekan tingkat ringan..."):
        time.sleep(1.5)
    st.warning(random.choice(roasts))

st.divider()

# Laugh Section
st.subheader("Kalau Kamu Ketawa Sekarang 🤣")
if st.button("Aku ngakak"):
    st.balloons()
    st.success("TERBUKTI. Kamu tidak sekuat itu 😝")

st.divider()

# Ending
st.markdown(
    """
    <p style='text-align:center;'>
    Website ini dibuat karena kamu ngeselin,<br>
    tapi anehnya… tetap pengen dijahilin 😌<br><br>
    <b>— Dari orang yang paling sabar ngadepin kamu</b>
    </p>
    """,
    unsafe_allow_html=True
)
