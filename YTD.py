from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Tilte: ", yt.title)

yd = yt.streams.get_highest_resolution()
yd.download('/Users/eliopikuli/Documents/YouTube Downloader')

print("Download is completed successfully\n")

# cd 'drag folder to download to'
# python3 YTD.py 'link'