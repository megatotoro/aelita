from django.contrib import admin

from .models import *

@admin.register(Doctors)
class DoctorsAdmin(admin.ModelAdmin):
    list_display = ['name', 'title']
    list_display_links = ['name',]
    search_fields = ['name', 'title']
    list_filter = ['name',]
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'id_cat']
    list_display_links = ['name', ]
    search_fields = ['name', 'id_cat' ]
    list_filter = ['name', 'id_cat']

@admin.register(Categorys)
class CategorysAdmin(admin.ModelAdmin):
    list_display = ['name',]
    list_display_links = ['name',]
    search_fields = ['name', ]
    list_filter = ['name',]
    prepopulated_fields = {"slug": ("name",)}
