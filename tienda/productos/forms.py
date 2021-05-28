from django import forms
from django.forms import fields

class ContactForm(forms.Form): #formulario cont todos los datos respectivos
	nombre= forms.CharField(max_length=500)
	numero_celular= forms.CharField(max_length=10)
	email = forms.EmailField(max_length = 150)
	mensage= forms.CharField(widget = forms.Textarea, max_length = 2000)