import streamlit as st
import base64
import os

st.set_page_config(page_title="DesbugaXuxu", layout="centered")

st.title("🧠 DesbugaXuxu")
st.markdown("### Aperte o play e desbugue sua mente em até 33 segundos")

AUDIO_DIR = "audios"

# Verifica se a pasta de áudios existe
if not os.path.exists(AUDIO_DIR):
    st.error("❌ Pasta de áudios não encontrada.")
    st.stop()

# Lista apenas arquivos .mp3 na pasta
audio_files = [f for f in os.listdir(AUDIO_DIR) if f.lower().endswith(".mp3")]

# Se não houver arquivos, avisa
if not audio_files:
    st.warning("⚠️ Nenhum áudio disponível.")
else:
    selected_audio = st.selectbox("Escolha um áudio", audio_files)
    audio_path = os.path.join(AUDIO_DIR, selected_audio)

    # Lê e toca o áudio
    with open(audio_path, "rb") as audio_file:
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")
        st.success(f"✅ Tocando agora: **{selected_audio}**")
