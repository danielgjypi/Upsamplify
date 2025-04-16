import streamlit as st
from enhance import enhance_audio
import os

st.title("AI Audio Upscaler")
st.write("Upload an MP3/WAV file to enhance its quality!")

uploaded_file = st.file_uploader("Choose a file", type=["mp3", "wav"])
if uploaded_file:
    st.audio(uploaded_file, format="audio/wav")

    if st.button("Upscale Audio"):
        with st.spinner("Enhancing audio..."):

            temp_input = "input/temp_upload.wav"
            with open(temp_input, "wb") as f:
                f.write(uploaded_file.getbuffer())

            output_path = "output/enhanced.wav"
            enhance_audio(temp_input, output_path)

            os.remove(temp_input)

        st.success("Done!")
        st.audio(output_path)