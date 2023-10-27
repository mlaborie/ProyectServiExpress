from django import forms
from .models import *

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nombre', 'apellido', 'correo', 'telefono', 'direccion', 'servicio', 'fecha', 'hora']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'placeholder': 'Apellido'}),
            'correo': forms.EmailInput(attrs={'placeholder': 'Correo electrónico'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Teléfono'}),
            'direccion': forms.TextInput(attrs={'placeholder': 'Dirección'}),
            'fecha': forms.DateInput(attrs={'placeholder': 'Fecha'}),
            'hora': forms.TimeInput(attrs={'placeholder': 'Hora'}),
}

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'  # Para incluir todos los campos del modelo




class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label='Nombre de usuario')
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')

