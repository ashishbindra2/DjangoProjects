from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index_view(request):
    request.session.set_test_cookie()
    return HttpResponse('<h1>index Page</h1>')


def check_view(request):
    if request.session.test_cookie_worked():
        print('cookies are working properly')
        request.session.delete_test_cookie()
        return HttpResponse('<h1>Checking Page</h1>')