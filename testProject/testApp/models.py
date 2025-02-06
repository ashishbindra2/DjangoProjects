from django.db import models


# Create your models here.

class TestApp(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, default='as')
    gender = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"id: {self.id} \n name: {self.name} \n gender: {self.gender}"


class EmployeeModel(models.Model):
    ename = models.CharField(max_length=100,null=True)
    esal = models.FloatField(max_length=100000000, null=True)
    ecity = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=100,unique=True,null=False)

    def __str__(self):
        return f"name: {self.ename} \n salary: {self.esal} \n email: {self.email} \n city: {self.ecity}"
