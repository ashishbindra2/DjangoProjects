from django import forms
from .models import MovieModel


class DateInput(forms.DateInput):
    input_type = 'date'


class MovieForm(forms.ModelForm):
    movie_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    release_date = forms.DateField(widget=DateInput(attrs={'class': 'form-control'}))
    hero_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    heroine_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    director_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    movie_ratings = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = MovieModel
        fields = "__all__"
        # fields = ['movie_name', 'release_date', 'hero_name', 'heroine_name', 'director_name', 'movie_ratings']
