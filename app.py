import streamlit as st
from transformers import pipeline, set_seed

st.set_page_config(page_title="REKA – Refleksi Kata", layout="centered")

# Load model ringan
@st.cache_resource
def load_model():
    generator = pipeline("text-generation", model="distilgpt2")
    set_seed(42)
    return generator

generator = load_model()

def buat_prompt(tema, input_user):
    tema = tema.lower()
    return f"Buat afirmasi bertema {tema} untuk seseorang yang berkata: \"{input_user}\".\nAfirmasi:"

st.markdown("<h1 style='text-align:center;'>REKA 🤍</h1>", unsafe_allow_html=True)
tema = st.selectbox("Pilih Tema Refleksi:", ["Motivasi", "Emosi", "Spiritual", "Netral"])
user_input = st.text_area("Tuliskan isi hatimu...")

if st.button("Refleksikan 🌱"):
    if user_input.strip():
        prompt = buat_prompt(tema, user_input)
        out = generator(prompt, max_length=80, num_return_sequences=1)[0]["generated_text"]
        afirmasi = out.replace(prompt, "").strip()
        st.markdown("### ✨ Afirmasi untukmu:")
        st.success(afirmasi)
    else:
        st.warning("Tolong tuliskan sesuatu dulu ya 😊")
