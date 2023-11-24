from django.shortcuts import render, redirect
from ServiExpress.models import *
from .forms import  ProveedorForm
from django.contrib import messages

def index(request):
    # Agrega aquí la lógica que desees para tu página de inicio
    return render(request, 'index.html')  # Aquí se renderiza un archivo HTML para la página de inicio

def checkout(request):
    return render(request, 'checkout.html') 

def base(request):
    return render(request, 'Home/base.html')

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
