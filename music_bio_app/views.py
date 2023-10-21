from django.shortcuts import render
from rest_framework import viewsets
from .models import Track, Album, Artist
from .serializers import TrackSerializer, AlbumSerializer, ArtistSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def get_queryset(self):
        sorting = self.request.query_params.get('sorting', None)
        queryset = Album.objects.all()
        if sorting:
            queryset = queryset.order_by(sorting)
        return queryset
