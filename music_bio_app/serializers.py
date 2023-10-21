from .models import Album, Artist, Track
from rest_framework import serializers


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    artist_name = serializers.StringRelatedField(source='artist', read_only=True)
    tracks = TrackSerializer(many=True, source='track_set', read_only=True)

    class Meta:
        model = Album
        fields = ('artist_name', 'tracks')

    def to_representation(self, instance):
        representation = super(AlbumSerializer, self).to_representation(instance)
        representation['album'] = f'{instance.album_name}[{instance.album_year}]'
        representation['artist@name'] = representation.pop('artist_name')
        representation['tracks'] = ', '.join([track['track_name'] for track in representation.pop('tracks')])
        return representation


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'
