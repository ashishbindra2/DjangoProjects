from django.urls import path
from  . import views
urlpatterns = [
    path('',views.index_view),
    path('list_movies/', views.list_movie_view),
    path('add_movie/', views.add_movie_view)
]