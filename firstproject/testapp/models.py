from django.db import models

# Create your models here.

class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=55)
    date = models.DateField( auto_now_add=True)
