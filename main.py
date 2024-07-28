from pathlib import Path
from datetime import datetime
import yt_modules
from starlette.middleware.cors import CORSMiddleware  # 追加
from pydantic import BaseModel  # リクエストbodyを定義するために必要
from typing import List  # ネストされたBodyを定義するために必要
from fastapi.responses import StreamingResponse
import zipfile
import io

import uvicorn

import os


from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

# CORSを回避するために追加（今回の肝）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,  # 追記により追加
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # 追記により追加
    allow_headers=["*"],  # 追記により追加
)


class Movies(BaseModel):
    url: str
    music_flg: bool
    movie_flg: bool


@app.post("/ydl-back")
async def root(movies: Movies):
    return {"message": "Hello World", "targeturl": movies.url}


@app.post("/ydl-back/yt_donwload")
def read_item(movies: Movies):
    yt_modules.download_yt(movies.url, movies.music_flg, movies.movie_flg)


@app.get("/ydl-back/get_file/{filename:path}")
async def get_file(filename: str):
    current = Path()
    file_path = current / "files" / filename

    response = FileResponse(path=file_path, filename=filename)

    return response


@app.get("/ydl-back/delete_file/{filename:path}")
async def deletes(filename: str):
    current = Path()
    file_path = current / "files" / filename

    # print(file_path)

    files = os.remove(file_path)


@app.get("/ydl-back/delete_all")
async def all_delete():
    current = Path()
    file_path = current / "files/"

    # print(file_path)
    for f in os.listdir(file_path):
        os.remove(
            os.path.join(file_path, f),
        )


@app.get("/ydl-back/file_info")
async def get_file():
    files = os.listdir("files")
    result_list = []
    movie_no = 1
    for file in files:
        # 音声用ファイルがもともとの名称ではスマホで再生できないので変換
        yt_modules.rename_file("files/" + file)
        movie_info = {"title": file, "no": movie_no}
        result_list.append(movie_info)
        movie_no = movie_no + 1

    print(result_list)
    return result_list

@app.get("/ydl-back/download_all")
async def donwload_all_files():
    current = Path()
    file_path = current / "files/"
    zip_filename = "all_files.zip"

    # デバッグ用のログを追加
    print(f"file_path: {file_path}")

    s = io.BytesIO()
    with zipfile.ZipFile(s, "w" , zipfile.ZIP_DEFLATED) as zf:
        for file in os.listdir(file_path):
            file_full_path = os.path.join(file_path, file)
            # デバッグ用のログを追加
            print(f"Adding file to zip: {file_full_path}")
            zf.write(file_full_path , arcname=file)
    s.seek(0)
    response = StreamingResponse(s, media_type="application/zip")
    response.headers["Content-Disposition"] = f"attachment; filename={zip_filename}"
    return response
    


if __name__ == "__main__":
    directory = "files"
    if not os.path.exists(directory):
        os.makedirs(directory)
    uvicorn.run(app, host="0.0.0.0", port=8000)