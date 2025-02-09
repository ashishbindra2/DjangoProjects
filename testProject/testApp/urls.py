from django.urls import re_path,path
from testApp import views

urlpatterns = [
    re_path("v1/", views.view1), # we can use a path
    re_path("v2/", views.view2),
    re_path("add_employee/", views.add_employee),
    re_path("get_employe_data/", views.get_employee),
    re_path("signup/", views.signup_view),
    path('login/', views.login_view, name='login')  # Add this line
 ]
