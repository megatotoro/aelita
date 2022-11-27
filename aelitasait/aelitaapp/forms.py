# sendemail/forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='ФИО', required=True)
    number = forms.IntegerField(label='Номер', required=True)
    date = forms.DateField(label='Дата записи', widget=forms.SelectDateWidget, required=True)
    message = forms.CharField(label='Комментарий', widget=forms.Textarea, required=False, max_length=200)