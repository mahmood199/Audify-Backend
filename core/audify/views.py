from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status

# Create your views here.
from rest_framework.decorators import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import AudioSerializer, ArtistSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken


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


@api_view(['GET'])
def get_all_artists(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response({'status': 200, 'message': "Successful", 'payload': serializer.data})


@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    validation_errors = {}

    if not username:
        validation_errors['username'] = 'Username is required'
    if not email:
        validation_errors['email'] = 'Email is required'
    if not password:
        validation_errors['password'] = 'Password is required'

    if User.objects.filter(username=username).exists():
        validation_errors['username'] = 'User with this username already exists'
    if User.objects.filter(email=email).exists():
        validation_errors['email'] = 'User with this email already exists'

    if validation_errors:
        return Response({'errors': validation_errors}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, email=email, password=password)

    return Response({'message': 'User created successfully', 'user': user}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def generate_jwt_token(request):
    try:
        user_id = request.data.get('user_id')
        id = request.data.get('id')

        print("User_id:-" + f"{user_id}")
        print("Id:-" + f"{id}")

        if not user_id or not id:
            raise ValueError("user_id or id are required")

        user = User.objects.get(id=id)

        refresh = RefreshToken.for_user(user)

        return Response({
            'status': 200,
            'message': "User data fetched successfully",
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

    except User.DoesNotExist:
        return Response({'error': 'User not found', 'status': '400'}, status=status.HTTP_404_NOT_FOUND)
