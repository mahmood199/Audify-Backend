from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import AudioSerializer, ArtistSerializer


@api_view(['GET'])
def get_all_audios(request):
    audios = Audio.objects.all()
    serializer = AudioSerializer(audios, many=True)
    return Response({'status': 200, 'message': "Some Message", 'payload': serializer.data})


@api_view(['POST'])
def add_audio(request):
    data = request.data
    serializer = AudioSerializer(data=data)

    if not serializer.is_valid():
        print(serializer.errors)
        return Response({'status': 403, 'payload': serializer.errors, 'message': "Something went wrong"})

    serializer.save()
    return Response({'status': 201, 'payload': serializer.data, 'message': "Data received"})


@api_view('GET')
def get_all_artists(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response({'status': 200, 'message': "Successful", 'payload': serializer.data})
