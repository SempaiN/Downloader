import streamlit as st

from downloader import download_audio

st.title("Audio")
link = st.text_input("Enter the link to the song")
file_name = st.text_input("Enter the name of the file")

if st.button("Download song"):
    if link and file_name:
        download_audio(url=link, file_name=file_name)
    else:
        st.write("Please enter a link and a filename for the song")