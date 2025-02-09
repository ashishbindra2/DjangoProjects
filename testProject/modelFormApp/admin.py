from django.contrib import admin
from .models import MovieModel


# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ['release_date', 'movie_name', 'hero_name', 'heroine_name', 'movie_ratings', 'director_name']


admin.site.register(MovieModel, MovieAdmin)
