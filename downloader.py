from pytube import YouTube

def download(url:str,file_name: str):
    yt = YouTube(url=url)
    audio = yt.streams.get_audio_only()
    audio.download(filename=f"{file_name}.mp3",output_path="./songs")

