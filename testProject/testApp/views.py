from django.shortcuts import render
from django.http import HttpResponse
from .models import EmployeeModel
from faker import Faker


# Create your views here.

def view1(request):
    return HttpResponse("<h1>view1</h1>")


def view2(request):
    return HttpResponse("<h1>view2</h12>")


def view3(request):
    return HttpResponse("<h1>view3</h1>")


def view4():
    return render("<h1>view4</h1>")


def add_employee(request):
    for _ in range(20):
        fack = Faker()
        name = fack.name()
        salary = float(fack.pricetag().replace(',', '')[1:])
        city = fack.city()
        email = fack.email()
        EmployeeModel.objects.get_or_create(ename=name,esal=salary,ecity=city,email=email)
    return HttpResponse("yo")


def get_employee(request):
    # employess = EmployeeModel.objects.all()
    # employess=EmployeeModel.objects.filter(esal__lt=3500)
    # employess=EmployeeModel.objects.filter(ename__startswith='A')
    # employess=EmployeeModel.objects.all().order_by('esal')
    # employess=EmployeeModel.objects.all().order_by('-esal')
    # employess = EmployeeModel.objects.values_list('ename')
    employess = EmployeeModel.objects.all().get(id=5)

    print(employess)
    return render(request,template_name='testApp/employeeInfo.html', context={"empList":employess})
