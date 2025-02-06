from django.shortcuts import render
from . import forms


# Create your views here.


def student_input_view(request):
    sent = False
    if request.method == 'POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            print('Form validation success and printing data')
            print('Name:', form.cleaned_data['name'])
            print('Marks:', form.cleaned_data['marks'])
            sent = True
    form = forms.StudentForm()

    return render(request, 'formApp/index.html', {'form': form, 'sent': sent})


def feedback_view(request):
    form = forms.FeedBackForm()
    if request.method == 'POST':
        form = forms.FeedBackForm(request.POST)
        if form.is_valid():
            print('Form Validation Success and printing information')
            print('Name:', form.cleaned_data['name'])
            print('Roll No:', form.cleaned_data['rollno'])
            print('Email:', form.cleaned_data['email'])
            print('FeedBack:', form.cleaned_data['feedback'])
    return render(request, 'formApp/feedback.html', {'form': form})


def signup_form_view(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            print('Basic Validation Completed and Printing Data')
            print('Name:', form.cleaned_data['name'])
            print('Password:', form.cleaned_data['password'])
            print('Email:', form.cleaned_data['email'])

    return render(request, 'formApp/signup.html', {'form': form})
