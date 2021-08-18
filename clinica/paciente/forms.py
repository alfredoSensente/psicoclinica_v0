"""Forms Paciente"""
#Django
from django import forms

#Models
from .models import Paciente
from .models import Direccion
from .models import TelefonoPaciente

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
            'nombre' : forms.TextInput(
                attrs={'type':'text', 'class':'form-control', 'id':'nombrePaciente'}
            ),
            'apellido' : forms.TextInput(
                attrs={'type':'text', 'class':'form-control', 'id':'apellidoPaciente'}
            ),
            'fecha_nacimiento' : forms.TextInput(
                attrs={'type':'date', 'class':'form-control', 'id':'fechaNacimientoPaciente'}
            ),
            'id_estado_civil' : forms.Select(
                attrs={'type':'text', 'class':'form-select', 'id':'estadoCivilPaciente'}
            ),
            'id_sexo' : forms.Select(
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
            'direccion' : forms.TextInput(
                attrs={'type':'text', 'class':'form-control', 'id':'direccionDireccion'}
            ),
            'id_municipio' : forms.Select(
                attrs={'type':'text', 'class':'form-select', 'id':'municipioDireccion'}
            ),
        }

class TelefonoPacienteForm(forms.ModelForm):
    """Form definition for TelefonoPaciente."""

    class Meta:
        """Meta definition for TelefonoPacienteform."""

        model = TelefonoPaciente
        fields = (
            'id_telefono_paciente',
            'telefono_paciente',
        )
        widgets = {
            'telefono_paciente' : forms.TextInput(
                attrs={'type':'number', 'class':'form-control', 'id':'telefonoTelefonoPaciente'}
            )
        }
