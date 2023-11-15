from django.shortcuts import render

def index(request):
    # Agrega aquí la lógica que desees para tu página de inicio
    return render(request, 'index.html')  # Aquí se renderiza un archivo HTML para la página de inicio


def checkout(request):
    return render(request, 'checkout.html')