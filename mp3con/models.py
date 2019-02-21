from __future__ import unicode_literals
import youtube_dl
import os
from django.db import models

# Create your models here
class Utuber(models.Model):
    name=models.CharField(max_length=130)

    def __str__(self):
        return self.name

    def save_db(self, urlss):
        check = Utuber(name=urlss)
        check.save()

    def download_mp3(self, song_url):
        ydl_opts = {
            'format': 'bestaudio/best',
            'noplaylist' : True,
            'postprocessors': [
                {'key': 'FFmpegExtractAudio',
                 'preferredcodec': 'mp3',
                 'preferredquality': '192'},
            ],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as dl:
            dl.download([song_url])

