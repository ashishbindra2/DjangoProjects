from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import Employee
from testapp import forms
# Create your views here.
def hello(request):
    return HttpResponse("AShish")
def thanks(request,std):
    return render(request,'testapp/thanks.html',{'name':std})

def studentregisterview(request):
    form = forms.StudentRegistration()
    if request.method == 'POST':
    # if request.post =='POST':
        form = forms.StudentRegistration(request.POST)
        if form.is_valid():
            print("Form Validation Success and printing feedback info !!")
            print("student Name:",form.cleaned_data['name'])
            print("student Marks:",form.cleaned_data['marks'])
            return thanks(request,form.cleaned_data['name'])#,{'name':form.cleaned_data['name']})

    return render(request,'testapp/register.html',{'form':form})

def index(request):
    emp = Employee.objects.all()
    return render(request,'testapp/index.html',{"name":"Ashish","emp":emp})
