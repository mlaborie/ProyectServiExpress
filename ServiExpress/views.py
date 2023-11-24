from django.shortcuts import render, redirect
from ServiExpress.models import *
from .forms import  ProveedorForm
from django.contrib import messages


from django.shortcuts import render, redirect
from ServiExpress.models import *
from .forms import  LoginForm, ProveedorForm
from django.contrib.auth import authenticate, login, logout
from django.http import  Http404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.views.generic import TemplateView
import datetime





def index(request):
    # Agrega aquí la lógica que desees para tu página de inicio
    return render(request, 'index.html')  # Aquí se renderiza un archivo HTML para la página de inicio

def checkout(request):
    return render(request, 'checkout.html') 


#Gestion De Proveedores

def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el proveedor en la base de datos
            messages.success(request, 'Proveedor creado con éxito.')  # Agrega un mensaje de éxito
            return redirect('../crear_proveedor')  # Redirige a la página principal o donde desees
    else:
        form = ProveedorForm()

    return render(request, 'ModuloGestionProveedores/crear_proveedor.html', {'form': form})

def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'ModuloGestionProveedores/lista_proveedores.html', {'proveedores': proveedores})

def editar_proveedor(request, proveedor_id):
    proveedor = Proveedor.objects.get(pk=proveedor_id)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedores')
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'ModuloGestionProveedores/editar_proveedor.html', {'form': form, 'proveedor': proveedor})

#Reserva

class CalendarView(TemplateView):
    template_name = 'ModuloReserva/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        today = datetime.date.today()
        year = int(self.request.GET.get('year', today.year))
        month = int(self.request.GET.get('month', today.month))

        # Lista de años para el campo desplegable
        years = range(today.year - 2, today.year + 5)

        # Lista de tuplas (número de mes, nombre de mes) para el campo desplegable
        months = [(i, datetime.date(2000, i, 1).strftime('%B')) for i in range(1, 13)]

        reservations = Reserva.objects.filter(fecha__year=year, fecha__month=month).select_related('cliente')

        calendar_data = {}
        for reserva in reservations:
            day = reserva.fecha.day
            if day not in calendar_data:
                calendar_data[day] = []

            # Asegúrate de que la relación 'cliente' esté cargada para acceder al Rut
                reserva.cliente.refresh_from_db()

            # Obtén el servicio asociado a la reserva
            servicio = reserva.servicio
            calendar_data[day].append({
                'fecha': reserva.fecha,
                'hora':reserva.hora,
                'cliente_nombre': reserva.cliente.nombre,
                'cliente_apellido': reserva.cliente.apellido,
                'cliente_rut': reserva.cliente.rut,
                'cliente_telefono': reserva.cliente.telefono,
                'cliente_correo': reserva.cliente.correo,
                'servicio_nombre': servicio.nombre,
                'servicio_descripcion': servicio.descripcion,
            })

        context['calendar_data'] = calendar_data
        context['month'] = datetime.date(year, month, 1).strftime('%B')
        context['year'] = year
        context['years'] = years
        context['months'] = months

        return context

def guardar_reserva(request):
    if request.method == "POST":
        # Obtener los datos del formulario
        cliente_rut = request.POST.get("cliente")
        fecha = request.POST.get("fecha")
        hora = request.POST.get("hora")
        servicio_id = request.POST.get("servicio")


        # Buscar el cliente y servicio seleccionados
        cliente = Cliente.objects.get(rut=cliente_rut)
        servicio = Servicio.objects.get(id_servicio=servicio_id)

        # Calcular el total (personaliza esto según tu lógica)
        total = servicio.precio

        # Crear la reserva
        reserva = Reserva(
            cliente=cliente,
            fecha=fecha,
            hora=hora,
            servicio=servicio,
            total=total,

        )

        # Guardar la reserva en la base de datos
        reserva.save()
        
        messages.success(request, 'La reserva fue registrada correctamente.')
        return redirect("../guardar_reserva")

    # Si el método de solicitud no es POST, renderiza el formulario
    clientes = Cliente.objects.all()
    servicios = Servicio.objects.all()


    return render(request, 'ModuloReserva/guardar_reserva.html', {"clientes": clientes, "servicios": servicios})

