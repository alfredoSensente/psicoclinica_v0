#Django
from django.shortcuts import render

#Models
from .models import Paciente

# Create your views here.
def index(request):
    """
    Devuelve un listado de pacientes
    """
    lista_paciente = Paciente.objects.all()
    context = {
        'lista_paciente' : lista_paciente,
    }
    return render(request, 'paciente/index.html', context)
