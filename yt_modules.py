from yt_dlp import YoutubeDL


def download_yt():
    f = open("dllist.txt", "r")
    datalist = f.readlines()
    # 動画用
    ydl_opts = {"format": "best", "outtmpl": "files/%(id)s.%(ext)s"}
    # 音声用
    # ydl_opts = {'format': 'bestaudio/best'}

    for data in datalist:
        print("***********開始*******************")
        print(data)
        with YoutubeDL(ydl_opts) as ydl:
            result = ydl.download([data])
            print(result)
