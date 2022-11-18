from django.contrib import admin

from .models import *

@admin.register(Doctors)
class DoctorsAdmin(admin.ModelAdmin):
    pass

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    pass

@admin.register(Categorys)
class CategorysAdmin(admin.ModelAdmin):
    pass
