# Django
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy

# Forms
from .forms import PacienteForm

# Models
from .models import Paciente

# Create your views here.


def index(request):
    """
    Devuelve un listado de pacientes
    """
    lista_paciente = Paciente.objects.all()
    context = {
        'lista_paciente': lista_paciente,
        'active_paciente': 'active',
    }
    return render(request, 'paciente/index.html', context)


def nuevo_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('paciente:index')
    else:
        return render(request, 'paciente/nuevo.html', context={'form': PacienteForm()})


def editar_paciente(request, pk):
    """
    update a patient
    """
    paciente_editar = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente_editar)
        if form.is_valid():
            form.save()
            return redirect('paciente:index')
    else:
        form = PacienteForm(instance=paciente_editar)
    context = {
        'form': form,
        'pk': pk,
    }
    return render(request, 'paciente/editar.html', context)


def detalle_paciente(request, pk):
    """
    Patient detail
    """
    paciente_detalle = get_object_or_404(Paciente, pk=pk)
    context = {
        'paciente': paciente_detalle
    }
    return render(request, 'paciente/detalle.html', context)


def borrar_paciente(request, pk):
    """
    Borrar a un paciente a traves de su pk
    """
    paciente_borrar = get_object_or_404(Paciente, pk=pk)

    if request.method == 'POST':
        paciente_borrar.delete()
        return render(request, 'paciente/borrar.html')
    else:
        context = {
            'paciente_borrar': paciente_borrar
        }
        return render(request, 'paciente/borrar.html', context)
