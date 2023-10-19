from django.shortcuts import render
from ServiExpress.models import *



def modulos_view(request):
    return render(request, 'Modulos.html')

def index(request):
    return render(request, 'index.html')

def FormularioReserva(request):
    return render(request, 'ModuloReserva/FormularioReserva.html')

