from django.db import models
from django.utils import timezone


# Create your models here.

class MovieModel(models.Model):
    release_date = models.DateField()
    movie_name = models.CharField(max_length=30)
    hero_name = models.CharField(max_length=30)
    heroine_name = models.CharField(max_length=30)
    movie_ratings = models.IntegerField()
    director_name = models.CharField(max_length=44)
