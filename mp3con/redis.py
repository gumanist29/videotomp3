from __future__ import unicode_literals
import youtube_dl
import os

from task22 import settings


def download_mp3(song_url):
    udl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,

        'postprocessors': [
            {'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
             'preferredquality': '192'},
                ],
           }

    with youtube_dl.YoutubeDL(udl_opts) as dl:
        os.chdir(settings.MEDIA_DIR)
        dl.download([song_url])