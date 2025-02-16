from django.contrib import admin
from .models import Company, Beer


# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'ceo']


class BeerAdmin(admin.ModelAdmin):
    list_display = ['name', 'taste', 'color', 'price']


admin.site.register(Company, CompanyAdmin)
admin.site.register(Beer, BeerAdmin)
