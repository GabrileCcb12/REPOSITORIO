from django.shortcuts import render
from .models import Departamento
# Create your views here.

from django.http import HttpResponse

def index(request):
    Departamentos = Departamento.objects.order_by('nombre')

    context = {'lista_departamentos' : Departamentos}
    #output = ', '.join([d.nombre for d in Departamentos])
    return render(request, 'index.html ', context)