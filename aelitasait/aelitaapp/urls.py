from django.urls import path
from .views import *

urlpatterns = [
    path('aelita/', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('doctors/', DoctorsListView.as_view(), name='doctors'),
    path('prices/', prices, name='prices'),
    path('aelita/<int:categorys_id>/', price, name='price'),
    path('success/', success_view, name='success'),
    path('ortopedia/', ortopedia, name='ortopedia'),
    path('doctors/<int:pk>', DoctorDetailView.as_view(), name='doctor-detail'),
]