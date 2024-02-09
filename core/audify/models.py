from django.db import models


# Create your models here.


class Audio(models.Model):
    title = models.CharField(max_length=200)
    release_year = models.IntegerField(default=2000)
    artist = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    download_url = models.CharField(max_length=200)

    LANGUAGE_CHOICES = [
        ('English', 'English'),
        ('Spanish', 'Spanish'),
    ]

    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)
    play_count = models.PositiveIntegerField(default=0)


class Artist(models.Model):
    title = models.CharField(max_length=200)

    LANGUAGE_CHOICES = [
        ('singer', 'Singer'),
        ('guitarist', 'Guitarist'),
    ]

    role = models.CharField(max_length=200, choices=LANGUAGE_CHOICES)
    type = models.CharField(max_length=200)
    url = models.CharField(max_length=200)


