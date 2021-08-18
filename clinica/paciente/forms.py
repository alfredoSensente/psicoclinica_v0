"""Forms Paciente"""
#Django
from django import forms
from django.forms import widgets

#Models
from .models import Paciente
from .models import Direccion

class PacienteForm(forms.ModelForm):
    """Form definition for Paciente."""

    class Meta:

        model = Paciente
        fields = (
            'nombre',
            'apellido',
            'fecha_nacimiento',
            'id_estado_civil',
            'id_sexo',
        )
        widgets = {
            'nombre':forms.TextInput(
                attrs={'type':'text', 'class':'form-control', 'id':'nombrePaciente'}
            ),
            'apellido':forms.TextInput(
                attrs={'type':'text', 'class':'form-control', 'id':'apellidoPaciente'}
            ),
            'fecha_nacimiento' : forms.TextInput(
                attrs={'type':'date', 'class':'form-control', 'id':'fechaNacimientoPaciente'}
            ),
            'id_estado_civil':forms.Select(
                attrs={'type':'text', 'class':'form-select', 'id':'estadoCivilPaciente'}
            ),
            'id_sexo':forms.Select(
                attrs={'type':'text', 'class':'form-select', 'id':'sexoPaciente'}
            ),
        }

class DireccionForm(forms.ModelForm):
    """Form definition for Direccion."""

    class Meta:
        """Meta definition for Direccionform."""

        model = Direccion
        fields = (
            'direccion',
            'id_municipio',
        )
        widgets = {
            'direccion':forms.TextInput(
                attrs={'type':'text', 'class':'form-control', 'id':'direccionDireccion'}
            ),
            'id_municipio':forms.Select(
                attrs={'type':'text', 'class':'form-select', 'id':'municipioDireccion'}
            ),
        }
