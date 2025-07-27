import streamlit as st
from transformers import pipeline, set_seed

st.set_page_config(page_title="REKA – Refleksi Kata", layout="centered")

# Load model GPT2 Indonesian dengan cache agar gak reload terus
@st.cache_resource
def load_model():
    generator = pipeline("text-generation", model="cahya/gpt2-small-indonesian")
    set_seed(42)
    return generator

generator = load_model()

def buat_prompt(tema, input_user):
    tema = tema.lower()
    return f"Buat afirmasi positif dan reflektif bertema {tema} untuk seseorang yang berkata: \"{input_user}\".\nAfirmasi:"

# UI Header
st.markdown(
    """
    <div style='text-align: center; padding: 2rem; background-color: #f5f1eb; border-radius: 15px;'>
        <h1 style='color: #5d473a;'>REKA</h1>
        <h3 style='color: #7a6655;'>Refleksi Kata</h3>
        <p style='color: #5d473a; font-size: 1.2rem;'>
            “Tempat di mana setiap kata menjadi cermin kecil untuk mengenali diri sendiri.”
        </p>
        <p style='margin-top: 2rem; font-size: 1rem; color: #7a6655;'>
            Oleh Ardina Latif
        </p>
    </div>
    """, unsafe_allow_html=True
)

st.markdown("---")

tema = st.selectbox("Pilih Tema Refleksi:", ["Motivasi", "Emosi", "Spiritual", "Netral"])
user_input = st.text_area("Tuliskan isi hatimu atau cerita singkatmu...")

if st.button("Refleksikan 🌿"):
    if user_input.strip() != "":
        prompt = buat_prompt(tema, user_input)
        output = generator(prompt, max_length=100, num_return_sequences=1)[0]["generated_text"]
        afirmasi = output.replace(prompt, "").strip()

        st.markdown("### ✨ Afirmasi untukmu:")
        st.success(afirmasi)
    else:
        st.warning("Coba tuliskan sesuatu dulu, ya 🌱")

