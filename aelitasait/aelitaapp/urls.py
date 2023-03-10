from django.urls import path
from django.views.decorators.cache import cache_page
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('doctors/', cache_page(60*2)(DoctorsListView.as_view()), name='doctors'),
    path('prices/', prices, name='prices'),
    path('price/<slug:price_slug>/', price, name='price'),
    path('success/', success_view, name='success'),
    path('ortopedia/', ortopedia, name='ortopedia'),
    path('doctors/<slug:slug>', cache_page(60*2)(DoctorDetailView.as_view()), name='doctor-detail'),
    path('success/', success_view, name='success')
]
