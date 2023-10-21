from django.db import models


class Album(models.Model):
    album_name = models.CharField(max_length=256)
    album_year = models.IntegerField()
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.album_name}, {self.album_year}'


class Artist(models.Model):
    artist_name = models.CharField(max_length=256)

    def __str__(self):
        return self.artist_name


class Track(models.Model):
    track_name = models.CharField(max_length=300)
    album = models.ForeignKey('Album', on_delete=models.CASCADE)

    def __str__(self):
        return self.track_name
