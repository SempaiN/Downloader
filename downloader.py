from pytube import YouTube
from torch import Stream

def download_audio(url:str,file_name: str):
    yt = YouTube(url=url)
    audio = yt.streams.get_audio_only()
    audio.download(filename=f"{file_name}.mp3",output_path="./files/audio")



def download_video(url:str,filename:str,hight_resolution: bool):
    yt = YouTube(url= url)
    video:
    if hight_resolution:
        video = yt.streams.get_highest_resolution()
    else:
        video = yt.streams.get_lowest_resolution()
    video.download()