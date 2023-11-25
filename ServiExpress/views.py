from django.shortcuts import render, redirect
from ServiExpress.models import *
from .forms import  ProveedorForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import RegistroForm
from .models import Perfil
from django.shortcuts import render

def index(request):
    # Agrega aquí la lógica que desees para tu página de inicio
    return render(request, 'index.html')  # Aquí se renderiza un archivo HTML para la página de inicio

def checkout(request):
    return render(request, 'checkout.html') 

def base(request):
    return render(request, 'Home/base.html')

def boleta(request):
    return render(request, 'MenuVendendor/ModuloRegistroBoleta/boleta.html')

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

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            tipo_usuario = form.cleaned_data['tipo_usuario']
            perfil = Perfil(usuario=user, tipo_usuario=tipo_usuario)
            perfil.save()
            login(request, user)
            return redirect('pagina_inicio')  # Cambia 'pagina_inicio' por la ruta de tu página principal
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

@login_required
def vista_cliente(request):
    # Tu lógica para clientes
    pass
@login_required
def vista_vendedor(request):
    # Tu lógica para vendedores
    pass
@login_required
def vista_admin(request):
    # Tu lógica para administradores
    pass

def vista_cliente(request):
    return render(request, 'cliente.html')

def vista_vendedor(request):
    return render(request, 'vendedor.html')

def vista_admin(request):
    return render(request, 'admin.html')

def vista_cliente(request):
    perfil = Perfil.objects.get(usuario=request.user)

    if perfil.tipo_usuario == Perfil.USUARIO_CLIENTE:
        # Lógica específica para clientes
        return render(request, 'cliente.html')
    else:
        # Redirigir a alguna página de error o a la página principal
        return render(request, 'error.html')

# Hacer lo mismo para las otras vistas (vista_vendedor y vista_admin)
