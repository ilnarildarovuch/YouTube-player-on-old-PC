from youtubesearchpython import VideosSearch
import os
from pytube import YouTube

os.chdir("D:/Program Files/VideoLAN/VLC/")

while True:
    os.chdir("vid")

    for i in os.listdir():
        os.remove(i)
    os.chdir("..")
    videosSearch = VideosSearch(input("Video: "), limit=1)
    videos = videosSearch.result()
    print(videos["result"][0]["link"])
    if input("To download? (y/n) ") == "y":
        res = input("Resolution [360p, 480p, 720p]:")
        if not res in ["360p", "480p", "720p"]:
            res = "360p"
        yt = YouTube(videos["result"][0]["link"]).streams.filter(res=res, only_video=False, only_audio=False)
        yt.first().download("./vid")
        os.system('vlc "vid/' + os.listdir("./vid")[0] + '"')