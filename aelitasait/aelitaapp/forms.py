# sendemail/forms.py
from django import forms
from .models import Doctors

class ContactForm(forms.Form):
    name = forms.CharField(label='ФИО', required=True, max_length=550,
                           widget=forms.TextInput(attrs={'class' : 'form-control input-border '}))
    number = forms.IntegerField(label='Номер', required=True,
                                widget=forms.TextInput(attrs={'class' : 'form-control input-border '}))
    doctor = forms.ModelChoiceField(queryset=Doctors.objects.all(), required=False, label='Врач',
                                    widget=forms.Select(attrs={'class' : 'form-control input-border'}))
    message = forms.CharField(label='Комментарий', widget=forms.Textarea(attrs={'class' : 'form-control input-border '}),
                              required=False, max_length=200)
    personal = forms.BooleanField(label='Даю согласие на обработку персональных данных')