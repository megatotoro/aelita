from django.shortcuts import render
from django.shortcuts import render
from django.views import generic

from .models import *

def index(request):
    cat = Categorys.objects.all()
    return render(request, 'aelitaapp/index.html', {'category': cat})

def contacts(request):
    return render(request, 'aelitaapp/contacts.html')

def prices(request):
    return render(request, 'aelitaapp/prices.html')

def price(request, categorys_id):
    price_cat = Price.object.filter(id_cat=categorys_id)
    return render(request, 'aelitapp/price.html', {'products': price_cat})

class DoctorsListView(generic.ListView):
    model = Doctors
    template_name = 'doctors_list.html'
    context_object_name = 'doctors'

class DoctorDetailView (generic.DetailView):
    model = Doctors
    template_name = 'doctor_detail.html'
    context_object_name = 'about_doctor'

