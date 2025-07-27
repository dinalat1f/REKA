import streamlit as st
from transformers import pipeline, set_seed

st.set_page_config(page_title="REKA 🤍", layout="centered")

@st.cache_resource
def load_model():
    return pipeline("text-generation", model="w11wo/indo-gpt2-small")

generator = load_model()

def buat_prompt(tema, isi):
    return f"Afirmasi {tema.lower()} untuk seseorang yang berkata: \"{isi}\"\nAfirmasi:"

st.title("REKA – Ruang Refleksi Karakter")
tema = st.selectbox("Tema Refleksi:", ["Motivasi", "Emosi", "Spiritual", "Netral"])
isi = st.text_area("Tuliskan perasaanmu...")

if st.button("Refleksikan"):
    prompt = buat_prompt(tema, isi)
    out = generator(prompt, max_new_tokens=80, do_sample=True, top_p=0.9, temperature=0.8)[0]["generated_text"]
    afirmasi = out.replace(prompt, "").strip()
    st.success(afirmasi or "Silakan tulis sedikit lebih panjang ya biar bisa muncul afirmasi 😊")
