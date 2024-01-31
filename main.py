from pathlib import Path
from datetime import datetime
import yt_modules

import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/yt_donwload")
def read_item():
    yt_modules.download_yt()
    # f = open("dllist.txt", "r")
    # datalist = f.readlines()
    # # 動画用
    # ydl_opts = {"format": "best", "outtmpl": "completed/%(id)s.%(ext)s"}
    # # 音声用
    # # ydl_opts = {'format': 'bestaudio/best'}

    # for data in datalist:
    #     print("***********開始*******************")
    #     print(data)
    #     with YoutubeDL(ydl_opts) as ydl:
    #         result = ydl.download([data])
    #         print(result)


@app.get("/get_file/{filename:path}")
async def get_file(filename: str):
    """任意ファイルのダウンロード"""
    current = Path()
    file_path = current / "files" / filename

    now = datetime.now()

    response = FileResponse(
        path=file_path, filename=f"download_{now.strftime('%Y%m%d%H%M%S')}_{filename}"
    )

    return response
