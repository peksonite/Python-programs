from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)

print("View: ", yt.views)

yd = yt.streams.get_audio_only()

# ADD FOLDER HERE
yd.download('/Users/kplachta/Desktop/python/yt downloader/audio')