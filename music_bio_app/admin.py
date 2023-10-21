from django.contrib import admin
from .models import Artist, Album, Track


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('artist_name',)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('album_name', 'album_year', 'artist')


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('track_name', 'album')
