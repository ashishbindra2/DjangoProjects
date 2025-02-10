from django.urls import path
from . import views

from django.conf.urls import include
urlpatterns = [
    path('java/', views.java_exams_view),
    path('accounts/', include('django.contrib.auth.urls')),

]