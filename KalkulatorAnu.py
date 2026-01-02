import streamlit as st

# -------------------------
# KONFIGURASI HALAMAN
# -------------------------
st.set_page_config(
    page_title="Kalkulator Sederhana",
    page_icon="🧮",
    layout="centered"
)

# -------------------------
# CSS ANIMATED BACKGROUND
# -------------------------
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(-45deg, #1e3c72, #2a5298, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }

    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .calculator-box {
        background: rgba(255, 255, 255, 0.92);
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.2);
        max-width: 400px;
        margin: auto;
    }

    .title {
        text-align: center;
        font-size: 32px;
        font-weight: bold;
        margin-bottom: 10px;
    }

    .subtitle {
        text-align: center;
        font-size: 14px;
        color: gray;
        margin-bottom: 25px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------
# KONTEN KALKULATOR
# -------------------------
st.markdown('<div class="calculator-box">', unsafe_allow_html=True)

st.markdown('<div class="title">🧮 Kalkulator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Kalkulator sederhana berbasis Streamlit</div>', unsafe_allow_html=True)

angka1 = st.number_input("Masukkan angka pertama", value=0.0)
angka2 = st.number_input("Masukkan angka kedua", value=0.0)

operasi = st.selectbox(
    "Pilih operasi",
    ["Penjumlahan (+)", "Pengurangan (-)", "Perkalian (×)", "Pembagian (÷)"]
)

if st.button("Hitung"):
    if operasi == "Penjumlahan (+)":
        hasil = angka1 + angka2
    elif operasi == "Pengurangan (-)":
        hasil = angka1 - angka2
    elif operasi == "Perkalian (×)":
        hasil = angka1 * angka2
    elif operasi == "Pembagian (÷)":
        if angka2 == 0:
            st.error("Tidak bisa membagi dengan nol!")
            hasil = None
        else:
            hasil = angka1 / angka2

    if hasil is not None:
        st.success(f"Hasil: **{hasil}**")

st.markdown('</div>', unsafe_allow_html=True)
