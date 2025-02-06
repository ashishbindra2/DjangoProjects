from django.contrib import admin
from testApp.models import EmployeeModel,TestApp


# Register your models here.


class TestAppAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender']


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["ename", "email", "ecity", "esal"]


admin.site.register(TestApp, TestAppAdmin)
admin.site.register(EmployeeModel, EmployeeAdmin)
