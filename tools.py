from pytube import YouTube


def get_resolutions(url: str) -> list[str]:
    yt = YouTube(url=url)
    streams = yt.streams
    resolutions = {
        stream.resolution for stream in streams if stream.resolution is not None
    }
    return sorted(resolutions)
