from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, CreateView, DeleteView, UpdateView
from django.http import HttpResponse

from django.views.generic import ListView, DetailView
from .models import Book, Company, Beer


# Create your views here.

class HelloWorldView(View):
    def get(self, request):
        return HttpResponse('<h1>This is from ClassBasedView</h1>')


class TemplateCBV(TemplateView):
    template_name = 'cbvApp/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['name'] = 'durga'
        context['age'] = 30
        return context


class BookListView(ListView):
    model = Book
    # context_object_name = 'book_list'
    # template_name = 'cbvApp/book_list.htm'


class CompanyListView(ListView):
    model = Company
    # default template_name is company_list.html
    # default context_object_name is company_list


class CompanyDetailView(DetailView):
    model = Company
    # default template_name is company_detail.html
    # default context_object_name is company or object


class CompanyCreateView(CreateView):
    model = Company
    fields = ('name', 'location', 'ceo')


class CompanyDeleteView(DeleteView):
    model = Company
    success_url = reverse_lazy('companies')


class BeerListView(ListView):
    model = Beer


class BeerDetailView(DetailView):
    model = Beer


class BeerCreateView(CreateView):
    model = Beer
    #fields=('name','taste','color','price')
    fields = '__all__'


class BeerUpdateView(UpdateView):
    model = Beer
    fields = ('taste', 'color', 'price')


class BeerDeleteView(DeleteView):
    model = Beer
    success_url = reverse_lazy('home')
