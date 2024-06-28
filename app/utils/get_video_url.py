from pytube import YouTube


def get_video_url(video_id):
    url = f"https://www.youtube.com/shorts?v={video_id}"
    yt = YouTube(url)
    video = yt.streams.filter(progressive=True, file_extension="mp4").first()
    print("video.url", video.url)
    return video.url
