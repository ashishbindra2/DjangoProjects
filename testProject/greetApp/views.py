from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def time():
    return datetime.now().strftime("%d/%m/%y, %H:%M:%S")


def geet_morning_view(request):
    # return HttpResponse("<h1>Good Morning!!!</h1>")
    greet = "Good Morning!!!"
    return render(request, template_name="greetApp/index.html", context={'greet': greet,'server_time': time()})


def geet_afternoon_view(request):
    # return HttpResponse("<h1>Good Afternoon!!!!</h1>")
    greet = "Good Afternoon!!!"

    return render(request, template_name="greetApp/index.html", context={'greet': greet,'server_time': time()})


def geet_evening_view(request):
    greet = "Good Evening!!!"

    # return HttpResponse("<h1>Good Evening!!!</h1>")
    return render(request, template_name="greetApp/index.html", context={'greet': greet,'server_time': time()})
