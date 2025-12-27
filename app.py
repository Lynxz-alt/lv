import streamlit as st
import time
import base64

# =========================
# Mobile First Love Website
# =========================
st.set_page_config(
    page_title="Untuk Luvi 💖",
    page_icon="💞",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- Mobile CSS Styling ---
st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: 'Helvetica Neue', sans-serif;
}

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
    max-width: 430px; /* Mobile width */
}

h1 {
    font-size: 1.8rem !important;
    text-align: center;
}

h4 {
    font-size: 1rem !important;
    text-align: center;
    color: #777;
}

p {
    font-size: 0.95rem !important;
    line-height: 1.6;
}

button[kind="primary"] {
    width: 100%;
    border-radius: 25px;
    padding: 0.6rem 0;
}

section[data-testid="stRadio"] label {
    font-size: 0.9rem;
}
</style>
""", unsafe_allow_html=True)

# --- Background Music ---


# Musik latar otomatis (wajib ada file music.mp3)

# autoplay_audio("music.mp3")

# =========================
# CONTENT
# =========================

st.markdown("""
<h1 style='color:#ff4b6e;'>💖 Untuk Luvi Hana Margareta 💖</h1>
<h4>Sebuah ruang kecil yang aman untuk perasaan</h4>
<hr>
""", unsafe_allow_html=True)

st.markdown(
    """
    <p>
    Hai Luvi 🌷<br><br>
    Aku tahu hubungan ini tidak selalu jelas arahnya.
    Kadang terasa dekat, kadang terasa menggantung.
    Tapi di tengah semua itu, aku ingin kamu tahu satu hal sederhana:
    <b>kamu berarti.</b>
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

st.subheader("Kalau hatimu boleh jujur 🤍")
choice = st.radio(
    "Saat membaca ini, apa yang paling kamu rasakan?",
    ["🌸 Aku merasa disayang", "🌙 Aku masih bingung, tapi hangat", "💗 Aku takut berharap, tapi ingin"],
)

if choice:
    st.info("Perasaanmu aman di sini.")

st.divider()

st.subheader("Surat kecil untukmu 💌")
if st.button("Buka suratnya"):
    with st.spinner("Menulis pelan dari hati..."):
        time.sleep(2)
    st.markdown(
        """
        > Aku tidak datang dengan tuntutan.
        > Aku datang dengan niat yang jujur.
        >
        > Jika suatu hari kamu ingin pergi,
        > aku akan mengikhlaskanmu tanpa menyakiti.
        > Tapi jika kamu memilih bertahan,
        > aku akan menjagamu dengan sepenuh hati.
        """
    )

st.divider()

st.subheader("Kalau kamu tersenyum sekarang 😊")
if st.button("Aku tersenyum"):
    st.balloons()
    st.success("Terima kasih sudah membaca sampai akhir 🤍")

st.markdown(
    """
    <p style='text-align:center;margin-top:30px;'>
    Tidak semua perasaan harus punya jawaban hari ini.<br>
    Tapi setiap perasaan pantas diperlakukan dengan lembut.<br><br>
    <b>— Dari seseorang yang peduli padamu</b>
    </p>
    """,
    unsafe_allow_html=True
)
