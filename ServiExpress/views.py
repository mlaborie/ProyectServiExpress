from django.shortcuts import render

def modulos_view(request):
    return render(request, 'Modulos.html')

def index(request):
    return render(request, 'index.html')
