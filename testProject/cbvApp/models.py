from django.db import models
from django.urls import reverse
from django.views.generic import UpdateView


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=30)
    pages = models.IntegerField()
    price = models.FloatField()


class Company(models.Model):
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=64)
    ceo = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})


class Employee(models.Model):
    eno = models.IntegerField()
    name = models.CharField(max_length=128)
    salary = models.FloatField()
    company = models.ForeignKey(Company, related_name='employees', on_delete=models.CASCADE)


class CompanyUpdateView(UpdateView):
    model = Company
    fields = ('name', 'ceo')


class Beer(models.Model):
    name=models.CharField(max_length=128)
    taste=models.CharField(max_length=128)
    color=models.CharField(max_length=128)
    price=models.FloatField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})
