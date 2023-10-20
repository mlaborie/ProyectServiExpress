from django.shortcuts import render, redirect
from ServiExpress.models import *
from .forms import ReservaForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import Http404




def modulos_view(request):
    return render(request, 'Modulos.html')

def index(request):
    return render(request, 'index.html')

def ReservaExitosa(request):
    return render(request, 'ModuloReserva/ReservaExitosa.html')

def BuscarReserva(request):
    return render(request, 'ModuloReserva/BuscarReserva.html')

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
                # Redirige al usuario después del inicio de sesión exitoso
                return redirect('inicio')  # 'inicio' es el nombre de la URL a la que deseas redirigir
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





from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

def is_superuser(user):
    return user.is_superuser


@login_required
@user_passes_test(is_superuser, login_url='no_permisos')
def administrar_usuarios(request):
    users = User.objects.all()
    return render(request, 'administrar_usuarios.html', {'users': users})

@login_required
@user_passes_test(is_superuser, login_url='no_permisos')
def crear_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        is_superuser = 'is_superuser' in request.POST
        first_name = request.POST.get('first_name')  # Obtener el valor del campo de nombre
        last_name = request.POST.get('last_name')  # Obtener el valor del campo de apellido
        email = request.POST.get('email')

        user = User.objects.create_user(username=username, password=password)
        user.is_superuser = is_superuser
        user.first_name = first_name  # Asignar el nombre
        user.last_name = last_name  # Asignar el apellido
        user.email = email
        user.save()
        return redirect('administrar_usuarios')
    return render(request, 'administrar_usuarios.html')

@login_required
@user_passes_test(is_superuser, login_url='no_permisos')
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


@login_required
@user_passes_test(is_superuser, login_url='no_permisos')
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

@login_required
@user_passes_test(is_superuser, login_url='no_permisos')
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



