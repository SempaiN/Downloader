import streamlit as st

from downloader import download_video

st.title("Video")
high_resolution = st.checkbox("High resolution")
link = st.text_input("Enter the link to the song")
file_name = st.text_input("Enter the name of the file")

if st.button("Download song"):
    if link and file_name:
        download_video(url=link,filename=file_name,high_resolution=high_resolution)
    else:
        st.write("Please enter a link and a filename for the song")
