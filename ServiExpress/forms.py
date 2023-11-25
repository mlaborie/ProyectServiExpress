from django import forms
from .models import *


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'  # Para incluir todos los campos del modelo

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label='Nombre de usuario')
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')



class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__' 

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__' 

