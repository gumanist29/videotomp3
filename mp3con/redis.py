from __future__ import unicode_literals
import youtube_dl
import requests
from django.http import HttpResponse, Http404
import os

from task22 import settings


def download_mp3(song_url):
    response = requests.get(song_url)
    if not response.status_code == 200:
        return Http404
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