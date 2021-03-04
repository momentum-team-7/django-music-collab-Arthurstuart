from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Album(models.Model):
    artist = models.CharField(max_length=280)
    # cover = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=280)
    album_release = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return f'{self.title} | {self.artist} | {self.album_release}'


class Artist(models.Model):
    name = models.CharField(max_length=150)
    record_label = models.CharField(max_length=150)

    def __str__(self):
        return {self.name}