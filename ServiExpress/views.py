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





def IndexAdministratoris(request):
    # Agrega aquí la lógica que desees para tu página de inicio
    return render(request, 'ModulusAdministratoris/IndexAdministratoris.html')  # Aquí se renderiza un archivo HTML para la página de inicio

def base(request):
    return render(request, 'Home/base.html')


#def IndexAdministratoris(request):
 #   return render(request, 'ModulusAdministratoris/IndexAdministratoris.html')



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

    return render(request, 'ModulusAdministratoris/ModuloGestionProveedores/crear_proveedor.html', {'form': form})

def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'ModulusAdministratoris/ModuloGestionProveedores/lista_proveedores.html', {'proveedores': proveedores})

def editar_proveedor(request, proveedor_id):
    proveedor = Proveedor.objects.get(pk=proveedor_id)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedores')
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'ModulusAdministratoris/ModuloGestionProveedores/editar_proveedor.html', {'form': form, 'proveedor': proveedor})

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

        total = servicio.precio

        # Crear la reserva
        reserva = Reserva(
            cliente=cliente,
            fecha=fecha,
            hora=hora,
            servicio=servicio,
            total=total,

        )

        reserva.save()
        
        messages.success(request, 'La reserva fue registrada correctamente.')
        return redirect("../guardar_reserva")

    # Si el método de solicitud no es POST, renderiza el formulario
    clientes = Cliente.objects.all()
    servicios = Servicio.objects.all()


    return render(request, 'ModuloReserva/guardar_reserva.html', {"clientes": clientes, "servicios": servicios})



#Servicios
from django.shortcuts import render, redirect,get_object_or_404
from .forms import ServicioForm, ProductoForm


def crear_servicio(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡El servicio se creó correctamente!')
            return redirect('crear_servicio')  
    else:
        form = ServicioForm()

    return render(request, 'ModulusAdministratoris/ModuloGestionServicios/crear_servicio.html', {'form': form})

def lista_servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'ModulusAdministratoris/ModuloGestionServicios/lista_servicios.html', {'servicios': servicios})

def editar_servicio(request, id_servicio):
    servicio = get_object_or_404(Servicio, id_servicio=id_servicio)

    if request.method == 'POST':
        form = ServicioForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            return redirect('lista_servicios') 
    else:
        form = ServicioForm(instance=servicio)

    return render(request, 'ModulusAdministratoris/ModuloGestionServicios/editar_servicio.html', {'form': form, 'servicio': servicio})

#Productos

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto creado correctamente.')
            return redirect('crear_producto')
    else:
        form = ProductoForm()

    return render(request, 'ModulusAdministratoris/ModuloGestionProductos/crear_producto.html', {'form': form})

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'ModulusAdministratoris/ModuloGestionProductos/lista_productos.html', {'productos': productos})

def editar_producto(request, id_producto):
    producto = get_object_or_404(Producto, id_producto=id_producto)

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'ModulusAdministratoris/ModuloGestionProductos/editar_producto.html', {'form': form, 'producto': producto})


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
        proveedor_id = Producto.objects.get(pk=producto_id).id_proveedor_id

        orden_compra = OrdenDeCompra.objects.create(
            id_proveedor=proveedor_id,
            id_producto=producto_id,
            cantidad=cantidad,
            precio=precio,
            empleado=request.user.id,
            comentario=f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
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

    return render(request, "ModuloGestionOC/generar_orden_compra.html", {
        "productos": productos,
        "productos_agregados": productos_agregados,
        "precio_total": precio_total
    })

def lista_ordenes_de_compra(request):
    ordenes_de_compra = OrdenDeCompra.objects.all()
    return render(request, 'ModuloGestionOC/lista_ordenes_de_compra.html', {'ordenes_de_compra': ordenes_de_compra})

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from .models import OrdenDeCompra

def detalle_orden_de_compra(request, orden_id):
    orden = get_object_or_404(OrdenDeCompra, pk=orden_id)

    # Crear un objeto HttpResponse con el tipo de contenido del PDF
    response = HttpResponse(content_type='application/pdf')
    # Establecer el nombre del archivo PDF
    response['Content-Disposition'] = f'filename=orden_de_compra_{orden.id_orden_de_pedido}.pdf'

    # Crear el objeto PDF, usando el objeto HttpResponse como su "archivo"
    p = canvas.Canvas(response)

    # Establecer el tamaño de la página
    p.setPageSize((400, 600))

    # Agregar contenido al PDF
    p.setFont("Helvetica", 12)
    p.drawString(50, 500, "Orden de Compra")
    p.drawString(50, 480, f'Orden de Compra ID: {orden.id_orden_de_pedido}')
    p.drawString(50, 460, f'Fecha: {orden.comentario}')  # Asegúrate de tener el campo 'fecha' en tu modelo
    p.drawString(50, 440, f'Proveedor: {orden.id_proveedor.razonSocial}')
    
    # Agregar detalles de la orden de compra
    p.drawString(50, 420, f'Producto: {orden.id_producto.nombre}')
    p.drawString(50, 400, f'Unidades: {orden.cantidad}')
    p.drawString(50, 380, f'Valor Unitario: {orden.precio}')
    #p.drawString(50, 360, f'Empleado: {orden.empleado}')

    # Calcular el total
    total = orden.cantidad * orden.precio
    p.drawString(50, 320, f'Total: ${total:.2f}')

    # Puedes seguir agregando más detalles y campos según sea necesario

    # Línea separadora
    p.line(50, 310, 350, 310)

    # Información adicional
    p.drawString(50, 290, "Gracias por su compra.")

    # Finalizar el PDF y cerrar el objeto Canvas
    p.showPage()
    p.save()

    return response


# views.py
from .forms import ClienteForm, EmpleadoForm, CustomUserCreationForm

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'cliente_form.html', {'form': form})

def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_empleados')
    else:
        form = EmpleadoForm()
    return render(request, 'empleado_form.html', {'form': form})

def crear_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = CustomUserCreationForm()
    return render(request, 'user_form.html', {'form': form})