from django.contrib import admin
from .models import *


# Register your models here.
class catadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    # list_display = ['name']


admin.site.register(categ, catadmin)


class proadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'category', 'price', 'mrp', 'offer', 'img', 'desc', 'available', 'stock']
    list_editable = ['category', 'price', 'mrp', 'offer', 'img', 'desc', 'available', 'stock']


admin.site.register(products, proadmin)
