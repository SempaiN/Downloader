import streamlit as st

st.title("Home Page")
st.subheader("Test song")
st.audio("./files/audio/testaudio.mp3",format="audio/mp3")
st.subheader("Test video")
st.video("./files/video/testvideo.mp4",format="video/mp4")
# url = st.text_input("Introduce la URL del video")
# filename  = st.text_input("Introduce el nombre de la canción")
# if st.button("Descargar canción"):
#     download(url= url,file_name= filename)