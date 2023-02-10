from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('doctors/', DoctorsListView.as_view(), name='doctors'),
    path('prices/', prices, name='prices'),
    path('price/<slug:price_slug>/', price, name='price'),
    path('success/', success_view, name='success'),
    path('ortopedia/', ortopedia, name='ortopedia'),
    path('doctors/<slug:slug>', DoctorDetailView.as_view(), name='doctor-detail'),
]
