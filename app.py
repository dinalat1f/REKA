import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="REKA – Refleksi Karakter", layout="centered")

@st.cache_resource
def load_model():
    return pipeline("text-generation", model="IzzulGod/GPT2-Indo-Instruct-Tuned")
generator = load_model()

def buat_prompt(tema, isi):
    return (
        f"Tema: {tema}\n"
        f"Pengguna: \"{isi}\"\n"
        "Buat cerita reflektif pendek, lalu lanjutkan dengan saran praktis.\n\n"
        "Cerita:\n"
        "Akhir cerita\n"
        "Saran:"
    )

tema = st.selectbox("Tema Refleksi:", ["Motivasi", "Emosi", "Spiritual", "Netral"])
isi = st.text_area("Tuliskan perasaan atau cerita singkatmu...")

if st.button("Refleksikan & Saran 🌿"):
    prompt = buat_prompt(tema, isi)
    hasil = generator(prompt,
                     max_new_tokens=150,
                     do_sample=True,
                     temperature=0.7,
                     top_p=0.9,
                     repetition_penalty=1.2)[0]["generated_text"]
    bagian = hasil.split("Saran:")
    cerita = bagian[0].replace(prompt, "").strip()
    saran = bagian[1].strip() if len(bagian)>1 else ""

    if cerita:
        st.markdown("## ✨ Cerita Reflektif:")
        st.write(cerita)
    if saran:
        st.markdown("## 📝 Saran untukmu:")
        st.write(saran)
