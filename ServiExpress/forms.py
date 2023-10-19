from django import forms
from .models import *

class ReservaForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    apellido = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Apellido'}))
    correo = forms.EmailField(max_length=50, required=True, widget=forms.EmailInput(attrs={'placeholder': 'Correo electrónico'}))
    telefono = forms.CharField(max_length=10, required=True, widget=forms.TextInput(attrs={'placeholder': 'Teléfono'}))
    direccion = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Dirección'}))

    servicio = forms.ModelChoiceField(queryset=Servicio.objects.all())  # Ajusta esto según tu modelo de Servicio
    fecha = forms.DateField(required=True, widget=forms.DateInput(attrs={'placeholder': 'Fecha'}))
    hora = forms.TimeField(required=True, widget=forms.TimeInput(attrs={'placeholder': 'Hora'}))
