"""Views Paciente"""
# Django
from django.shortcuts import redirect, render, get_object_or_404

# Forms
from .forms import PacienteForm
from .forms import TelefonoPacienteForm
from .forms import DireccionForm
from .forms import EmailPacienteForm

# Models
from .models import Paciente

# Create your views here.


def index(request):
    """Devuelve un listado de pacientes"""
    if request.method == 'POST':
        if request.POST['opcion-paciente'] == 'nombre':
            lista_paciente = Paciente.objects.filter(
                nombre__icontains=request.POST['busqueda-paciente']
            )
        elif request.POST['opcion-paciente'] == 'apellido':
            lista_paciente = Paciente.objects.filter(
                apellido__icontains=request.POST['busqueda-paciente']
            )
        elif request.POST['opcion-paciente'] == 'sexo':
            lista_paciente = Paciente.objects.filter(
                id_sexo__sexo__icontains=request.POST['busqueda-paciente']
            )
    else:
        lista_paciente = Paciente.objects.all()
    context = {
        'lista_paciente': lista_paciente,
    }
    return render(request, 'paciente/index.html', context)


def nuevo_paciente(request):
    """Agrega un nuevo paciente atraves de un formulario"""

    if request.method == 'POST':
        form_paciente = PacienteForm(request.POST)
        form_direccion = DireccionForm(request.POST)
        form_telefono = TelefonoPacienteForm(request.POST)
        form_email = EmailPacienteForm(request.POST)
        if (form_paciente.is_valid() and
            form_direccion.is_valid() and
            form_telefono.is_valid() and
            form_email.is_valid()
        ):
            paciente = form_paciente.save(commit=False)
            telefono_paciente = form_telefono.save(commit=False)
            email_paciente = form_email.save(commit=False)

            direccion = form_direccion.save()

            paciente.id_direccion = direccion
            paciente.save()

            telefono_paciente.id_paciente = paciente
            telefono_paciente.save()

            email_paciente.id_paciente = paciente
            email_paciente.save()

            return redirect('paciente:index')
    else:
        context={
            'form_paciente' : PacienteForm(),
            'form_direccion' : DireccionForm(),
            'form_telefono' : TelefonoPacienteForm(),
            'form_email' : EmailPacienteForm(),
        }
        return render(request, 'paciente/nuevo.html', context)


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
