from fastapi import FastAPI
from yt_dlp import YoutubeDL

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/yt_donwload")
def read_item():
    f = open("dllist.txt", "r")
    datalist = f.readlines()
    # 動画用
    ydl_opts = {"format": "best", "outtmpl": "completed/%(id)s.%(ext)s"}
    # 音声用
    # ydl_opts = {'format': 'bestaudio/best'}

    for data in datalist:
        print("***********開始*******************")
        print(data)
        with YoutubeDL(ydl_opts) as ydl:
            result = ydl.download([data])
            print(result)
