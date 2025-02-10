from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm, ItemAddForm, AgeForm, NameForm, GFForm


# Create your views here.


def index_view(request):
    request.session.set_test_cookie()
    return HttpResponse('<h1>index Page</h1>')


def check_view(request):
    if request.session.test_cookie_worked():
        print('cookies are working properly')
        request.session.delete_test_cookie()
        return HttpResponse('<h1>Checking Page</h1>')


def count_view(request):
    if 'count' in request.COOKIES:
        new_count = int(request.COOKIES['count']) + 1
    else:
        new_count = 1

    response = render(request, 'sessionApp/count.html', {'count': new_count})
    response.set_cookie('count', new_count)
    return response


def home_view(request):
    form = LoginForm()
    return render(request, 'sessionApp/home.html', {'form': form})


def date_time_view(request):
    # form=LoginForm(request.GET)
    name = request.GET['name']
    response = render(request, 'sessionApp/datetime.html', {'name': name})
    response.set_cookie('name', name)
    return response


def name_view(request):
    return render(request, 'sessionApp/name.html')


def age_view(request):
    name = request.GET['name']
    response = render(request, 'sessionApp/age.html', {'name': name})
    response.set_cookie('name', name)
    return response


def gf_view(request):
    age = request.GET['age']
    name = request.COOKIES['name']
    response = render(request, 'sessionApp/gf.html', {'name': name})
    response.set_cookie('age', age)
    return response


def results_view(request):
    name = request.COOKIES['name']
    age = request.COOKIES['age']
    gfname = request.GET['gfname']
    print(gfname)
    response = render(request, 'sessionApp/results.html', {'name': name, 'age': age, 'gfname': gfname})
    response.set_cookie('gfname', gfname)
    return response


def result_view(request):
    name = request.COOKIES['name']
    date_time = datetime.now()
    my_dict = {'name': name, 'date_time': date_time}
    return render(request, 'sessionApp/result.html', my_dict)


# shopping cart app
def index(request):
    return render(request, 'sessionApp/index.html')


def add_item(request):
    form = ItemAddForm()
    response = render(request, 'sessionApp/additem.html', {'form': form})

    if request.method == 'POST':
        form = ItemAddForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['itemname']
            quantity = form.cleaned_data['quantity']
            response.set_cookie(name, quantity, 180)
    return response


def display_item_view(request):
    return render(request, "sessionApp/showitems.html")


# session

def page_count_view(request):
    count = request.session.get('count', 0)
    new_count = count + 1
    request.session['count'] = new_count

    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    return render(request, 'sessionApp/pageCount.html', {'count': new_count})


def name_session_view(request):
    form = NameForm()
    return render(request, 'sessionApp/name.html', {'form': form})


def age_session_view(request):
    name = request.GET['name']
    request.session['name'] = name
    form = AgeForm()
    return render(request, 'sessionApp/age.html', {'form': form})


def gf_session_view(request):
    age = request.GET['age']
    request.session['age'] = age
    form = GFForm()
    return render(request, 'sessionApp/gf.html', {'form': form})


def results_session_view(request):
    gf = request.GET['gf']
    request.session['gf'] = gf
    return render(request, 'sessionApp/results.html')


def add_item_view(request):
    form = ItemAddForm()

    if request.method == 'POST':
        form = ItemAddForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['itemname']
            quantity = form.cleaned_data['quantity']
            request.session[name] = quantity
    return render(request, 'sessionApp/additem.html', {'form': form})


def display_items_view(request):
    return render(request, 'sessionApp/displayitems.html')
