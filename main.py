from pathlib import Path
from datetime import datetime
import yt_modules
from starlette.middleware.cors import CORSMiddleware  # 追加

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
    allow_methods=["*"],  # 追記により追加
    allow_headers=["*"],  # 追記により追加
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/yt_donwload/{url:path}")
def read_item(url: str):
    yt_modules.download_yt(url)


@app.get("/get_file/{filename:path}")
async def get_file(filename: str):
    current = Path()
    file_path = current / "files" / filename

    response = FileResponse(path=file_path, filename=filename)

    return response


@app.get("/delete_file/{filename:path}")
async def get_file(filename: str):
    current = Path()
    file_path = current / "files" / filename

    # print(file_path)

    files = os.remove(file_path)


@app.get("/file_info")
async def get_file():
    files = os.listdir("files")
    result_list = []
    for file in files:
        yt_modules.rename_file("files/" + file)
        movie_info = {"title": file}
        result_list.append(movie_info)

    print(result_list)
    return result_list
