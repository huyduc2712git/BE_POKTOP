import time
from flask import jsonify


def generate_video_urls(video_urls):
    for url in video_urls:
        yield f"{jsonify({'videoUrl': url})}\n"
        time.sleep(1)  # Giả lập việc gửi dữ liệu theo thời gian
