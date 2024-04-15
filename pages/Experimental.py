import streamlit as st
from pytube import YouTube
from downloader import download_video_resolution
from tools import get_resolutions

st.title("Experimental")

url = st.text_input("Enter the link")
filename = st.text_input("Enter the filename")

if "resolutions" not in st.session_state:
    st.session_state["resolutions"] = []

if st.button("Check resolutions"):
    if url:
        st.session_state["resolutions"] = get_resolutions(url=url)
        selected_resolution = st.selectbox(
            "Resolutions", st.session_state["resolutions"]
        )
        st.text(f"You selected {selected_resolution}")
        

    else:
        st.write("Please enter a YouTube video URL")
else:
    selected_resolution = st.selectbox("Resolutions", st.session_state["resolutions"])
    st.text(f"You selected {selected_resolution}")

if st.button("Download"):
    if selected_resolution and url and filename:
        download_video_resolution(filename=filename,resolution=selected_resolution,url=url)
    else:
        st.write("Please complete all inputs")