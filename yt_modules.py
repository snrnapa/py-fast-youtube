from yt_dlp import YoutubeDL

from pathlib import Path
from datetime import datetime

from fastapi.responses import FileResponse
import os


def read_youtube_info(movie_url: str):
    ydl_opts = {
        "writeautomaticsub": "False",
    }
    with YoutubeDL(ydl_opts) as ydl:
        res = ydl.extract_info(movie_url, download=False)


def download_yt(movie_url: str):
    file_name = "%(title)s.%(ext)s"

    file_path = "files/{}".format(file_name)

    # 動画用
    # ydl_opts = {"format": "best", "outtmpl": file_path}
    # 音声用
    ydl_opts = {"format": "bestaudio/best", "outtmpl": file_path}

    print("***********開始*******************")
    print(movie_url)
    with YoutubeDL(ydl_opts) as ydl:
        result = ydl.download([movie_url])


def rename_file(file_name: str):
    after_name = file_name.replace(" ", "")
    os.rename(file_name, after_name)
    print(after_name)
