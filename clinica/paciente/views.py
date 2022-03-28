"""Views Paciente"""
# Django
from django.shortcuts import get_list_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

# Forms
from .forms import PacienteForm
from .forms import DireccionForm
from .forms import ReferenciaForm
from .forms import ContactoForm

# Models
from .models import Contacto, Paciente, Direccion, Referencia

# Create your views here.


def index(request):
    """Devuelve un listado de pacientes"""
    if request.method == 'POST':
        if request.POST['opcion-paciente'] == 'nombre_paciente':
            lista_paciente = Paciente.objects.filter(
                nombre_paciente__icontains=request.POST['busqueda-paciente']
            )
        elif request.POST['opcion-paciente'] == 'apellido_paciente':
            lista_paciente = Paciente.objects.filter(
                apellido_paciente__icontains=request.POST['busqueda-paciente']
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
        form_referencia = ReferenciaForm(request.POST)
        form_contacto = ContactoForm(request.POST)
        if (form_paciente.is_valid() and
                form_direccion.is_valid() and
                form_referencia.is_valid() and
                form_contacto.is_valid()
                ):
            paciente = form_paciente.save(commit=False)
            contacto = form_contacto.save(commit=False)
            referencia = form_referencia.save(commit=False)
            # Guarda direccion
            direccion = form_direccion.save()
            # Guarda paciente
            paciente.id_direccion = direccion
            paciente.save()
            # Guarda referencia
            referencia.id_paciente = paciente
            referencia.save()
            # Guarda contacto
            contacto.id_paciente = paciente
            contacto.save()

            return redirect('paciente:index')
    else:
        context = {
            'form_paciente': PacienteForm(),
            'form_direccion': DireccionForm(),
            'form_referencia': ReferenciaForm(),
            'form_contacto': ContactoForm(),
        }
        return render(request, 'paciente/nuevo.html', context)


def editar_paciente(request, id_paciente):
    """update a patient"""

    paciente_editar = get_object_or_404(Paciente, pk=id_paciente)
    direccion_paciente = Direccion.objects.get(
        pk=paciente_editar.id_direccion.pk)
    referencia_paciente = Referencia.objects.get(
        id_paciente=paciente_editar.pk)
    contacto_paciente = Contacto.objects.filter(id_paciente=paciente_editar.pk)

    if request.method == 'POST':
        form_paciente = PacienteForm(request.POST, instance=paciente_editar)
        form_direccion = DireccionForm(
            request.POST, instance=direccion_paciente)
        form_referencia = ReferenciaForm(
            request.POST, instance=referencia_paciente)
        form_contacto = ContactoForm(request.POST, instance=contacto_paciente)
        if (form_paciente.is_valid() and
                form_direccion.is_valid() and
                form_referencia.is_valid() and
                form_contacto.is_valid()
                ):
            paciente = form_paciente.save(commit=False)
            contacto = form_contacto.save(commit=False)
            referencia = form_referencia.save(commit=False)
            # Guarda direccion
            direccion = form_direccion.save()
            # Guarda paciente
            paciente.id_direccion = direccion
            paciente.save()
            # Guarda referencia
            referencia.id_paciente = paciente
            referencia.save()
            # Guarda contacto
            contacto.id_paciente = paciente
            contacto.save()

            return redirect('paciente:index')

    context = {
        'form_paciente': PacienteForm(instance=paciente_editar),
        'form_direccion': DireccionForm(instance=direccion_paciente),
        'form_referencia': ReferenciaForm(instance=referencia_paciente),
        'form_contacto': contacto_paciente,
    }
    return render(request, 'paciente/editar.html', context)


def detalle_paciente(request, id_paciente):
    """Patient detail"""

    paciente_detalle = get_object_or_404(Paciente, pk=id_paciente)
    lista_contactos = get_list_or_404(Contacto, id_paciente=id_paciente)
    context = {
        'paciente': paciente_detalle,
        'lista_contactos': lista_contactos,
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


class ContactoCreate(generic.CreateView):
    """Contact Create"""
    model = Contacto
    form_class = ContactoForm
    template_name = 'paciente/contacto/nuevo.html'

    def get_success_url(self):
        return reverse_lazy(
            'paciente:detalle',
            kwargs={'id_paciente': self.kwargs['id_paciente']}
        )

    def form_valid(self, form):
        """Contacto Form"""
        paciente = Paciente.objects.get(pk=self.kwargs['id_paciente'])
        form.instance.id_paciente = paciente
        return super().form_valid(form)


class ContactoUpdate(generic.UpdateView):
    """Contact Update"""
    model = Contacto
    form_class = ContactoForm
    template_name = 'paciente/contacto/editar.html'

    def get_success_url(self):
        return reverse_lazy(
            'paciente:detalle',
            kwargs={'id_paciente': self.kwargs['id_paciente']}
        )

    def form_valid(self, form):
        """Contacto Form"""
        paciente = Paciente.objects.get(pk=self.kwargs['id_paciente'])
        form.instance.id_paciente = paciente
        return super().form_valid(form)
