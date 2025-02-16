from django.db import models


# Create your models here.
class TodoListModel(models.Model):
    task = models.CharField(null=False,max_length=100)

