from rest_framework import routers
from .views import AlbumViewSet

album_router = routers.DefaultRouter()
album_router.register(r'album', AlbumViewSet, basename='album')
