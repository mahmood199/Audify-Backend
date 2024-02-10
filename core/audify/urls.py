

from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('get_audios', get_all_audios),
    path('add_audio', add_audio),
    path('get_artists', get_all_artists),
]
