from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth.views import LogoutView

# from django.conf.urls import include

urlpatterns = [
    path('', views.home_page_view),
    path('java/', views.java_exams_view),
    path('accounts/', include('django.contrib.auth.urls')),
    path('python/', views.python_exams_view),
    path('aptitude/', views.aptitude_exams_view),
    path('logout/', views.logout_view),
    path('signup/', views.signup_view),

]
