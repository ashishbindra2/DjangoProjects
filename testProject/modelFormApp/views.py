from django.shortcuts import render
from .models import MovieModel
from .forms import MovieForm


# Create your views here.

def index_view(request):
    return render(request, "modelFormApp/index.html")


def add_movie_view(request):
    form = MovieForm()

    if request.method == 'POST':
        form = MovieForm(request.POST)

        if form.is_valid():
            form.save()
        return index_view(request)
    return render(request, 'modelFormApp/add_movie.html', {"form":form})


def list_movie_view(request):
    movies_list = MovieModel.objects.all().order_by('-movie_ratings')
    return render(request, 'modelFormApp/list_movies.html', {"movies_list": movies_list})
