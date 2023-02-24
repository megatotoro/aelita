from django.shortcuts import render
from django.views import generic
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect
from .forms import ContactForm

from .models import *


def index(request):
    cat = Categorys.objects.all()
    # если метод GET, вернем форму
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        # если метод POST, проверим форму и отправим письмо
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            number = form.cleaned_data['number']
            doctor = form.cleaned_data['doctor']
            message = form.cleaned_data['message']
            message_post = 'врач {doctor} сообщение {message}'
            try:
                send_mail(f'{name} от {number}', message_post,
                          'k1rsanova.tan@yandex.ru', ['k1rsanova.tan@yandex.ru'])
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return redirect('success')
    else:
        return HttpResponse('Неверный запрос.')
    return render(request, 'aelitaapp/index.html', {'category': cat, 'form':form})


def contacts(request):
    # если метод GET, вернем форму
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        # если метод POST, проверим форму и отправим письмо
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            number = form.cleaned_data['number']
            #doctor = form.cleaned_data['doctor']
            message_post = 'врач {doctor} сообщение {message}'
            try:
                send_mail(f'{name} от {number}', message_post,
                          'k1rsanova.tan@yandex.ru', ['k1rsanova.tan@yandex.ru'])
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return redirect('success')
    else:
        return HttpResponse('Неверный запрос.')
    return render(request, "aelitaapp/contacts.html", {'form': form})

    #if request.method == 'POST':
    #    form = ContactForm(request.POST)
    #   if form.is_valid():
    #        print(form.cleaned_data)
    # else:
    #    form = ContactForm
    #return render(request, 'aelitaapp/contacts.html', {'form': form})


def success_view(request):
    return render(request, 'aelitaapp/success.html')


def ortopedia(request):
    return render(request, 'aelitaapp/ortopedia.html')


def price(request, price_slug):
    name_cat = Categorys.objects.get(slug=price_slug)
    price_cat = Price.objects.filter(id_cat=name_cat.pk)
    context = {'products': price_cat, 'name_cat': name_cat}
    return render(request, 'aelitaapp/price.html', context)
    allow_empty = False #вызывает 404 если категории не существует


def prices(request):
    cat = Categorys.objects.all()
    # если метод GET, вернем форму
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        # если метод POST, проверим форму и отправим письмо
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            number = form.cleaned_data['number']
            # doctor = form.cleaned_data['doctor']
            message_post = 'врач {doctor} сообщение {message}'
            try:
                send_mail(f'{name} от {number}', message_post,
                          'k1rsanova.tan@yandex.ru', ['k1rsanova.tan@yandex.ru'])
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return redirect('success')
    else:
        return HttpResponse('Неверный запрос.')
    return render(request, 'aelitaapp/prices.html', {'cat': cat, 'form':form})


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
