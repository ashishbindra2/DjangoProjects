from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def home_page_view(request):
    return render(request, 'loginApp/home.html')


@login_required
def java_exams_view(request):
    return render(request, 'loginApp/java.html')


@login_required
def python_exams_view(request):
    return render(request, 'loginApp/pythonexams.html')


@login_required
def aptitude_exams_view(request):
    return render(request, 'loginApp/aptitudeexams.html')


def logout_view(request):
    return render(request, 'loginApp/logout.html')
