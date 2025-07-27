import os
import streamlit as st
import openai

st.set_page_config(page_title="REKA – Ruang Refleksi Karakter", layout="centered")

openai.api_key = st.secrets.get("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY"))

def chat_gpt_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # bisa ganti ke "gpt-4.1" jika tersedia
        messages=[
            {"role": "system", "content": "Kamu adalah asisten yang empatik dan menenangkan dalam bahasa Indonesia."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=300,
        top_p=0.9,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].message.content.strip()

st.title("REKA – Ruang Refleksi & Saran GPT")

tema = st.selectbox("Pilih Tema Refleksi:", ["Motivasi", "Emosi", "Spiritual", "Netral"])
isi = st.text_area("Tuliskan apa yang kamu rasakan...")

if st.button("Refleksikan & Saran"):
    prompt = f"[Tema: {tema}]\nPengguna: \"{isi}\"\nBalas sebagai cerita reflektif singkat dan beri saran praktis yang hangat."
    balasan = chat_gpt_response(prompt)
    st.markdown("### ✨ Jawaban dari GPT:")
    st.write(balasan)
