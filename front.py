import streamlit as st
from downloader import download
st.title("Download Audio")
url = st.text_input("Introduce la URL del video")
filename  = st.text_input("Introduce el nombre de la canción")
if st.button("Descargar canción"):
    download(url= url,file_name= filename)