import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="REKA – Refleksi & Saran", layout="centered")

@st.cache_resource
def load_model():
    return pipeline("text-generation", model="IzzulGod/GPT2-Indo-chat-tuned")

generator = load_model()

def buat_prompt(tema, isi):
    return (
        f"Tema: {tema}\n"
        f"Pengguna berkata: \"{isi}\"\n"
        "Buat narasi cerita pendek yang reflektif dan dilanjutkan dengan saran praktis.\n"
        "Cerita pendek:\nAkhir cerita\n"
        "Saran:"
    )

st.title("REKA – Ruang Refleksi Karakter")
tema = st.selectbox("Pilih Tema Refleksi:", ["Motivasi", "Emosi", "Spiritual", "Netral"])
isi = st.text_area("Tuliskan isi hatimu atau ceritamu...")

if st.button("Refleksikan & Saran 🌿"):
    prompt = buat_prompt(tema, isi)
    hasil = generator(
        prompt,
        max_new_tokens=120,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        repetition_penalty=1.2
    )[0]["generated_text"]
    soal_split = hasil.split("Saran:")
    cerita = soal_split[0].replace(prompt, "").strip()
    saran = soal_split[1].strip() if len(soal_split) > 1 else ""
    if cerita:
        st.markdown("## ✨ Cerita Reflektif:")
        st.write(cerita)
    if saran:
        st.markdown("## 📝 Saran untukmu:")
        st.write(saran)
