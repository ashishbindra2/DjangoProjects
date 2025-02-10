from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm


# Create your views here.
def home_page_view(request):
    return render(request, 'loginApp/home.html')


@login_required
def java_exams_view(request):
    return render(request, 'loginApp/javaexams.html')


@login_required
def python_exams_view(request):
    return render(request, 'loginApp/pythonexams.html')


@login_required
def aptitude_exams_view(request):
    return render(request, 'loginApp/aptitudeexams.html')


def logout_view(request):
    return render(request, 'loginApp/logout.html')


def signup_view(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/loginApp/accounts/login')
    return render(request, 'loginApp/signup.html', {'form': form})
