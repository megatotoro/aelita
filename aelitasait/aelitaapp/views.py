from django.shortcuts import render
from django.views import generic
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect
from .forms import ContactForm

from .models import *


def index(request):
    cat = Categorys.objects.all()
    return render(request, 'aelitaapp/index.html', {'category': cat})


def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = ContactForm
    return render(request, 'aelitaapp/contacts.html', {'form': form})


def success_view(request):
    return HttpResponse('Приняли! Спасибо за вашу заявку.')


def ortopedia(request):
    return render(request, 'aelitaapp/ortopedia.html')


def price(request, price_slug):
    name_cat = Categorys.objects.get(slug=price_slug)
    price_cat = Price.objects.filter(id_cat=name_cat.pk)
    context = {'products': price_cat, 'name_cat': name_cat}
    return render(request, 'aelitaapp/price.html', context)


def prices(request):
    cat = Categorys.objects.all()
    return render(request, 'aelitaapp/prices.html', {'cat': cat})


class DoctorsListView(generic.ListView):
    model = Doctors
    template_name = 'doctors_list.html'
    context_object_name = 'doctors'


class DoctorDetailView(generic.DetailView):
    model = Doctors
    template_name = 'doctor_detail.html'
    context_object_name = 'about_doctor'
    slug_field = 'slug'


def pageNotFound(request, exception):
    return render(request, 'aelitaapp/404,html', status=404)
