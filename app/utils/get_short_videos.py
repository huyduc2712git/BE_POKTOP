from googleapiclient.discovery import build
from get_video_url import get_video_url

# Thay YOUR_API_KEY bằng API key bạn đã đăng ký
api_key = "AIzaSyAqKHqjJ3swzaM0D_JHWzhXbRCbrYTJkBg"
youtube = build("youtube", "v3", developerKey=api_key)


# Hàm để lấy danh sách video ngắn
def get_short_videos(query, max_results):
    request = youtube.search().list(
        part="snippet",
        q=query
        + " #shorts",  # Adding #shorts to the query to increase likelihood of getting Shorts
        type="video",
        videoDuration="short",
        maxResults=max_results,
    )
    response = request.execute()

    videos = []
    for item in response["items"]:
        video_info = {
            "title": item["snippet"]["title"],
            "videoId": item["id"]["videoId"],
            "description": item["snippet"]["description"],
            "thumbnail": item["snippet"]["thumbnails"]["default"]["url"],
        }
        videos.append(video_info)

    return videos


# Ví dụ: Lấy danh sách các video ngắn liên quan đến từ khóa "Python"
short_videos = get_short_videos("Python", max_results=50)
for video in short_videos:
    print("video", video)
    print(f"Title: {video['title']}")
    print(f"Video ID: {video['videoId']}")
    videoId = video["videoId"]
    print(f"Description: {video['description']}")
    print(f"Thumbnail URL: {video['thumbnail']}\n")
    get_video_url(videoId)
