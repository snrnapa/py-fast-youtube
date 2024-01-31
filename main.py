from pathlib import Path
from datetime import datetime
import yt_modules

import uvicorn

import os


from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


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

    now = datetime.now()

    response = FileResponse(
        path=file_path, filename=f"download_{now.strftime('%Y%m%d%H%M%S')}_{filename}"
    )

    return response


@app.get("/file_info")
async def get_file():
    files = os.listdir("files")
    result_list = []
    for file in files:
        movie_info = {"title": file}
        result_list.append(movie_info)

    print(result_list)
    return result_list
