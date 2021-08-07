"""Views Paciente"""
# Django
from django.shortcuts import redirect, render, get_object_or_404

# Forms
from .forms import PacienteForm

# Models
from .models import Paciente

# Create your views here.


def index(request):
    """Devuelve un listado de pacientes"""
    lista_paciente = Paciente.objects.all()
    context = {
        'lista_paciente': lista_paciente,
        'active_paciente': 'active',
    }
    return render(request, 'paciente/index.html', context)


def nuevo_paciente(request):
    """Agrega un nuevo paciente atraves de un formulario"""

    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('paciente:index')
    else:
        return render(request, 'paciente/nuevo.html', context={'form': PacienteForm()})


def editar_paciente(request, id_paciente):
    """update a patient"""

    paciente_editar = get_object_or_404(Paciente, pk=id_paciente)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente_editar)
        if form.is_valid():
            form.save()
            return redirect('paciente:index')
    else:
        form = PacienteForm(instance=paciente_editar)
    context = {
        'form': form,
    }
    return render(request, 'paciente/editar.html', context)


def detalle_paciente(request, id_paciente):
    """Patient detail"""

    paciente_detalle = get_object_or_404(Paciente, pk=id_paciente)
    context = {
        'paciente': paciente_detalle
    }
    return render(request, 'paciente/detalle.html', context)


def borrar_paciente(request, id_paciente):
    """Borrar a un paciente a traves de su id_paciente"""

    paciente_borrar = get_object_or_404(Paciente, pk=id_paciente)
    if request.method == 'POST':
        paciente_borrar.delete()
        return render(request, 'paciente/borrar.html')
    context = {
        'paciente_borrar': paciente_borrar
    }
    return render(request, 'paciente/borrar.html', context)
