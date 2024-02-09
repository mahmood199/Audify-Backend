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
