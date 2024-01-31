from yt_dlp import YoutubeDL

from pathlib import Path
from datetime import datetime

from fastapi.responses import FileResponse


def download_yt(movie_url: str):
    # 動画用
    file_name = "%(id)s.%(ext)s"

    file_path = "files/{}".format(file_name)
    print(file_path)

    ydl_opts = {"format": "best", "outtmpl": file_path}
    # 音声用
    # ydl_opts = {'format': 'bestaudio/best'}

    print("***********開始*******************")
    print(movie_url)
    with YoutubeDL(ydl_opts) as ydl:
        result = ydl.download([movie_url])
        print(result)


async def get_file(filename: str):
    """任意ファイルのダウンロード"""
    current = Path()
    file_path = current / "files" / filename

    now = datetime.now()

    response = FileResponse(
        path=file_path, filename=f"download_{now.strftime('%Y%m%d%H%M%S')}_{filename}"
    )

    return response
