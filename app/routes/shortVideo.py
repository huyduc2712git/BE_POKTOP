from flask import Response

import app
from app.utils.generate_video_urls import generate_video_urls


@app.route("/video-urls", methods=["GET"])
def video_urls_stream():
    return Response(generate_video_urls(), content_type="application/json")
