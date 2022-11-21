from django.shortcuts import render
from django.views import generic
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

from .models import *

def index(request):
    cat = Categorys.objects.all()
    return render(request, 'aelitaapp/index.html', {'category': cat})

def contacts(request):
    # если метод GET, вернем форму
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        # если метод POST, проверим форму и отправим письмо
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(f'{subject} от {from_email}', message,
                          'k1rsanova.tan@yandex.ru', ['k1rsanova.tan@yandex.ru'])
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return redirect('success')
    else:
        return HttpResponse('Неверный запрос.')
    return render(request, "aelitaapp/contacts.html", {'form': form})


def success_view(request):
    return HttpResponse('Приняли! Спасибо за вашу заявку.')

def ortopedia(request):
    return render(request, 'aelitaapp/ortopedia.html')

def price(request, categorys_id):
    price_cat = Price.objects.filter(id_cat=categorys_id)
    name_cat = Categorys.objects.get(pk=categorys_id)
    context = {'products': price_cat, 'name_cat': name_cat}
    return render(request, 'aelitaapp/price.html', context)

def prices(request):
    cat = Categorys.objects.all()
    return render(request, 'aelitaapp/prices.html', {'cat': cat})

class DoctorsListView(generic.ListView):
    model = Doctors
    template_name = 'doctors_list.html'
    context_object_name = 'doctors'

class DoctorDetailView (generic.DetailView):
    model = Doctors
    template_name = 'doctor_detail.html'
    context_object_name = 'about_doctor'

