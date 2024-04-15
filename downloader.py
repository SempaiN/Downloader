from pytube import YouTube
from pytube import Stream


def download_audio(url: str, file_name: str):
    yt = YouTube(url=url)
    audio = yt.streams.get_audio_only()
    audio.download(filename=f"{file_name}.mp3", output_path="./files/audio")


def download_video(url: str, filename: str, high_resolution: bool):
    yt = YouTube(url=url)
    video: Stream
    if high_resolution:
        video = yt.streams.get_highest_resolution()
    else:
        video = yt.streams.get_lowest_resolution()
    video.download(filename=f"{filename}.mp4", output_path="./files/video")


def download_video_resolution(filename: str, url: str, resolution: str):
    yt = YouTube(url=url)
    video = yt.streams.get_by_resolution(resolution=resolution)
    video.download(filename=f"{filename}.mp4",output_path="./files/video")