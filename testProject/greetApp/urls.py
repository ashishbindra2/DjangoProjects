from django.urls import re_path
from . import views

urlpatterns = [
    re_path("greet_morning/", views.geet_morning_view), # we can use path
    re_path("greet_afternoon/", views.geet_afternoon_view),
    re_path("greet_evening/", views.geet_evening_view),
]
