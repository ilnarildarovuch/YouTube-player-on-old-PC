from youtubesearchpython import VideosSearch
import os
from pytube import YouTube

while True:
    os.chdir("D:/Program Files/VideoLAN/VLC/vid")

    for i in os.listdir():
        os.remove(i)
    os.chdir("..")
    videosSearch = VideosSearch(input("Видео: "), limit=1)
    videos = videosSearch.result()
    print(videos["result"][0]["link"])
    yt = YouTube(videos["result"][0]["link"]).streams.filter(res="360p", only_video=False, only_audio=False)
    yt.first().download("./vid")
    os.system('vlc "vid/' + os.listdir("./vid")[0] + '"')
    input()