from django.urls import path

from .models import CompanyUpdateView
from .views import HelloWorldView, BookListView, TemplateCBV, CompanyDetailView, CompanyListView, CompanyCreateView, \
    CompanyDeleteView, BeerListView, BeerDetailView, BeerCreateView, BeerUpdateView, BeerDeleteView

urlpatterns = [
    path('', HelloWorldView.as_view()),
    path('book/', BookListView.as_view()),
    path('temp/', TemplateCBV.as_view()),
    path('companies/', CompanyListView.as_view(), name='companies'),
    # path('(?P<pk>\d+/', CompanyDetailView.as_view(),name='detail')
    path('<int:pk>/', CompanyDetailView.as_view(), name='detail'),
    path('create/', CompanyCreateView.as_view(), name='create'),
    path('update/<int:pk>/', CompanyUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', CompanyDeleteView.as_view(), name='delete'),

    path('beer/', BeerListView.as_view(), name='home'),
    path('beer/<pk>', BeerDetailView.as_view(), name='details'),
    path('beer/create/', BeerCreateView.as_view()),
    path('beer/update/<pk>/', BeerUpdateView.as_view()),
    path('beer/delete/<pk>/', BeerDeleteView.as_view()),
]
