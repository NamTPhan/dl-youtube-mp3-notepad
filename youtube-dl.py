from __future__ import unicode_literals
import youtube_dl
import os

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': os.getcwd() + '/songs/%(title)s.%(ext)s',
}

youtubeLinks = open('youtube-links.txt', 'r')

for song in youtubeLinks:
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([song])

youtubeLinks.close()
