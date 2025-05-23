import os
import streamlit as st
from utils.utils import extract_audio_from_mp4_url
from utils.classifier import detect_accent

st.title("audio accent classification")
AUDIO_PATH = os.path.join(os.getcwd(), "audio", "audio.mp3")

# Create the form
with st.form("registration_form"):
    video_url = st.text_input("video url")
    
    # Submit button
    submitted = st.form_submit_button("Submit")

# Handle submission
if submitted:
    with st.spinner("Processing video and predicting accent..."):
        extract_audio_from_mp4_url(video_url, AUDIO_PATH)
        percentage_score, country_accent = detect_accent(AUDIO_PATH)


    st.success("successfully processed!")
    st.write("Accent Classification:", f"{country_accent}")
    st.write("Confidence Score:", f"{percentage_score:.2f}%")
    st.write("Summary:", f"Your accent is a/an {country_accent} accent.")
