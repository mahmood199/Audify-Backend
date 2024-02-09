from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import *
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def hello_world(request):
    return Response({'status': 200, 'message': "Some Message"})
