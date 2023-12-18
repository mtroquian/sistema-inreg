from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import NumeroInforme, NumeroIncr
from .forms import NumeroInformeForm, GenerarNumeroForm
def inicio(request):
    return render(request, 'html/inicio.html')

def nosotros(request):
    return render(request, 'html/nosotros.html')


def index(request):
    numeros = NumeroIncr.objects.all()

    return render(request, 'numeros/index.html', {'numeroinforme': numeros})

def abc(request):
    if request.method == 'POST':
        form = GenerarNumeroForm(request.POST)
        
        if form.is_valid():
            nuevo_numero = form.generar_numero()
            form.instance.numero_informe = nuevo_numero
            
                
            form.save()
            return redirect('index')  # Redirige a donde necesites después de generar el número
            
    else:
        form = GenerarNumeroForm()

    return render(request, 'numeros/abc.html', {'form': form})


def editar(request):
    return render(request, 'numeros/editar.html')


def crear(request):
    formulario = NumeroInformeForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('index')
    return render(request, 'numeros/crear.html', {'formulario': formulario})


def generar_numero_incremental(request):
    if request.method == 'POST':
        form = GenerarNumeroForm(request.POST)
        if form.is_valid():
            nuevo_numero = form.generar_numero()
            NumeroIncr.objects.create(numero_informe=nuevo_numero)
            return redirect('index')  # Redirige a donde necesites después de generar el número
    else:
        form = GenerarNumeroForm()

    return render(request, 'template.html', {'form': form})