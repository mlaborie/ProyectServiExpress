from django.shortcuts import render, redirect
from ServiExpress.models import *
from .forms import ReservaForm


def modulos_view(request):
    return render(request, 'Modulos.html')

def index(request):
    return render(request, 'index.html')

def ReservaExitosa(request):
    return render(request, 'ModuloReserva/ReservaExitosa.html')

def FormularioReserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save()
            return redirect('reserva_exitosa')  # Redirige a la página de éxito utilizando el nombre de la URL
    else:
        form = ReservaForm()

    servicios = Servicio.objects.all()

    return render(request, 'ModuloReserva/FormularioReserva.html', {'servicios': servicios, 'form': form})


