from .models import Album, Artist, Track
from rest_framework import serializers


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    artist_name = serializers.StringRelatedField(source='artist', read_only=True)
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(AlbumSerializer, self).to_representation(instance)
        representation['album'] = f'{instance.album_name}[{instance.album_year}]'
        representation['artist@name'] = representation.pop('artist_name')
        return representation


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'
