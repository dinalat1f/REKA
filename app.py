import streamlit as st
from transformers import pipeline, set_seed

st.set_page_config(page_title="REKA – Ruang Refleksi Karakter", layout="centered")

@st.cache_resource
def load_model():
    return pipeline(
        "text-generation",
        model="IzzulGod/GPT2-Indo-chat-tuned"
    )

generator = load_model()

def buat_prompt(tema, isi):
    return (
        f"Tema: {tema}\n"
        f"Pengguna berkata: \"{isi}\"\n"
        "Buat afirmasi yang hangat, menenangkan, dan reflektif dalam Bahasa Indonesia.\n"
        "Afirmasi:"
    )

st.title("REKA – Ruang Refleksi Karakter")
tema = st.selectbox("Tema Refleksi:", ["Motivasi", "Emosi", "Spiritual", "Netral"])
isi = st.text_area("Tuliskan perasaanmu...")

if st.button("Refleksikan 🌿"):
    prompt = buat_prompt(tema, isi)
    out = generator(
        prompt,
        max_new_tokens=80,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        repetition_penalty=1.2
    )[0]["generated_text"]
    afirmasi = out.replace(prompt, "").strip()
    st.success(afirmasi)
