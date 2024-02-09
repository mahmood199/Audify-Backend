from rest_framework import serializers

from .models import *


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = [
            'id',
            'title',
            'release_year',
            'artist',
            'description',
            'url',
            'download_url',
            'language',
            'play_count'
        ]

    def validate(self, data):
        validation_errors = {}

        if not data.get('title') or data.get('title').strip() == '':
            validation_errors['title'] = "Title is mandatory"
        if not data.get('release_year') and int(data.get('release_year')) == 2000:
            validation_errors['release_year'] = "Release Year is mandatory"
        if not data.get('artist') or data.get('artist').strip() == '':
            validation_errors['artist'] = "Artist is mandatory"
        if not data.get('url') or data.get('url').strip() == '':
            validation_errors['url'] = "Url is mandatory"
        if not data.get('download_url') or data.get('download_url').strip() == '':
            validation_errors['download_url'] = "Download Url is mandatory"
        if not data.get('language') or data.get('language').strip() == '':
            validation_errors['language'] = "Language is mandatory"

        return data


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'