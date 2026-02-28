from pytubefix import YouTube
from pytubefix import Search
import os
search = input("Digite o Nome Do Vídeo a Baixar: ")
s = Search(search)
if len(s.results) > 0:
    video = s.results[0]
url = video.watch_url
yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)

print(yt.title)
ys = yt.streams.get_highest_resolution()
ys.download()
os.system(f"mpv --vo=tct '{yt.title}.mp4'")