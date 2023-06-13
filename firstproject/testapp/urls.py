from django.urls import path
from testapp import views

urlpatterns =[
    path('hello/',views.hello),
    path('',views.index),
    path('register',views.studentregisterview),
    path('thanks',views.thanks),

]
