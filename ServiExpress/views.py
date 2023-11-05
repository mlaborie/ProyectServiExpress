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


def modulos_view(request):
    return render(request, 'Modulos.html')

def index(request):
    return render(request, 'index.html')

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
        years = range(today.year - 5, today.year + 5)

        # Lista de tuplas (número de mes, nombre de mes) para el campo desplegable
        months = [(i, datetime.date(2000, i, 1).strftime('%B')) for i in range(1, 13)]

        reservations = Reserva.objects.filter(fecha__year=year, fecha__month=month)

        calendar_data = {}
        for reserva in reservations:
            day = reserva.fecha.day
            if day not in calendar_data:
                calendar_data[day] = []
            # Obtén el servicio asociado a la reserva
            servicio = reserva.servicio
            calendar_data[day].append({
                'fecha': reserva.fecha,
                'cliente': reserva.cliente.nombre,
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

        # Puedes agregar más lógica aquí, como redireccionar a una página de éxito
        return redirect("../guardar_reserva")  # Ajusta "pagina_exito" según tu configuración

    # Si el método de solicitud no es POST, renderiza el formulario
    clientes = Cliente.objects.all()
    servicios = Servicio.objects.all()


    return render(request, 'ModuloReserva/guardar_reserva.html', {"clientes": clientes, "servicios": servicios})









































def Login(request):
    return render(request, 'Login.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('http://127.0.0.1:8000/')  # 'inicio' es el nombre de la URL a la que deseas redirigir
            else:
                # Mostrar un mensaje de error al usuario
                return render(request, 'login.html', {'form': form, 'error_message': 'Credenciales inválidas'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    # Redirige al usuario después del cierre de sesión
    return redirect('login')  # 'login' es el nombre de la URL de inicio de sesión

# Otras vistas relacionadas con tus modelos pueden ir aquí.





def is_superuser(user):
    return user.is_superuser

#@login_required
#@user_passes_test(is_superuser, login_url='no_permisos')
def administrar_usuarios(request):
    users = User.objects.all()
    return render(request, 'administrar_usuarios.html', {'users': users})

#@login_required
#@user_passes_test(is_superuser, login_url='no_permisos')
def crear_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        is_superuser = 'is_superuser' in request.POST
        first_name = request.POST.get('first_name') 
        last_name = request.POST.get('last_name')  
        email = request.POST.get('email')

        user = User.objects.create_user(username=username, password=password)
        user.is_superuser = is_superuser
        user.first_name = first_name  
        user.last_name = last_name  
        user.email = email
        user.save()
        return redirect('administrar_usuarios')
    return render(request, 'administrar_usuarios.html')

#@login_required
#@user_passes_test(is_superuser, login_url='no_permisos')
def editar_usuario(request):
    if request.method == 'POST':
        user_id = request.POST.get('user')
        password = request.POST.get('password')
        is_superuser = 'is_superuser' in request.POST
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        try:
            selected_user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise Http404("El usuario no existe")

        # Actualiza los datos del usuario seleccionado
        selected_user.is_superuser = is_superuser
        if password:
            selected_user.set_password(password)
        selected_user.first_name = first_name
        selected_user.last_name = last_name
        selected_user.email = email
        selected_user.save()

        return redirect('administrar_usuarios')
    else:
        users = User.objects.all()
        return render(request, 'administrar_usuarios.html', {'users': users})

#@login_required
#@user_passes_test(is_superuser, login_url='no_permisos')
def deshabilitar_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            user = User.objects.get(username=username)
            user.is_active = False  # Deshabilitar el usuario
            user.save()
        except User.DoesNotExist:
            pass  # El usuario no existe
    return redirect('administrar_usuarios')

#@login_required
#@user_passes_test(is_superuser, login_url='no_permisos')
def habilitar_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            user = User.objects.get(username=username)
            user.is_active = True  # Habilitar el usuario
            user.save()
        except User.DoesNotExist:
            pass  # El usuario no existe
    return redirect('administrar_usuarios')







# Modulo Ordenes de compra

from decimal import Decimal
from django.shortcuts import render
from .models import Producto, OrdenDeCompra

def producto_to_dict(producto):
    return {
        'id_producto': producto.id_producto,
        'nombre': producto.nombre,
        'descripcion': producto.descripcion,
        'precio': float(producto.precio),
        # Agrega más campos si es necesario
    }

def dict_to_producto(diccionario):
    return Producto(
        id_producto=diccionario['id_producto'],
        nombre=diccionario['nombre'],
        descripcion=diccionario['descripcion'],
        precio=Decimal(str(diccioniario['precio'])),
        # Reconstruye más campos si es necesario
    )

def calcular_precio_total(productos_agregados):
    total = Decimal('0.00')
    for producto in productos_agregados:
        subtotal = Decimal(str(producto['subtotal']))
        total += subtotal
    return total

def generar_orden_compra(request):
    productos = Producto.objects.all()

    # Elimina la lista de productos agregados en la sesión al cargar la página
    if request.method == "GET":
        request.session.pop('productos_agregados', None)

    productos_agregados = request.session.get('productos_agregados', [])

    if request.method == "POST":
        producto_id = request.POST.get("id_producto")
        cantidad = request.POST.get("cantidad")
        precio = request.POST.get("precio")
        comentario = request.POST.get("comentario")
        proveedor_id = Producto.objects.get(pk=producto_id).id_proveedor_id

        orden_compra = OrdenDeCompra.objects.create(
            id_proveedor=proveedor_id,
            id_producto=producto_id,
            cantidad=cantidad,
            precio=precio,
            empleado=request.user.id,
            comentario=comentario
        )

        producto = Producto.objects.get(pk=producto_id)
        productos_agregados.append({
            'producto': producto_to_dict(producto),
            'cantidad': cantidad,
            'precio': float(precio),
            'subtotal': float(cantidad) * float(precio)
        })

        request.session['productos_agregados'] = productos_agregados

    precio_total = calcular_precio_total(productos_agregados)

    return render(request, "generar_orden_compra.html", {
        "productos": productos,
        "productos_agregados": productos_agregados,
        "precio_total": precio_total
    })

    #return render(request, 'crear_orden_de_compra.html', {'proveedores': proveedores, 'productos': productos})

