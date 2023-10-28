from django import forms
from .models import *


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'  # Para incluir todos los campos del modelo

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label='Nombre de usuario')
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')



class ReservaForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), to_field_name="rut")
    servicios = forms.ModelMultipleChoiceField(queryset=Servicio.objects.all(), to_field_name="nombre")

    class Meta:
        model = Reserva
        exclude = ['correo', 'telefono', 'direccion', 'nombre', 'apellido', 'total']

    def save(self, commit=True):
        reserva = super().save(commit=False)
        cliente = self.cleaned_data['cliente']
        reserva.correo = cliente.correo
        reserva.telefono = cliente.telefono
        reserva.direccion = cliente.direccion
        reserva.nombre = cliente.nombre
        reserva.apellido = cliente.apellido
        reserva.total = sum(servicio.precio for servicio in self.cleaned_data['servicios'])
        if commit:
            reserva.save()
        return reserva