"""Forms Paciente"""
#Django
from django import forms

#Models
from .models import Paciente
from .models import Direccion
from .models import Referencia
from .models import Contacto


class PacienteForm(forms.ModelForm):
    """Form definition for Paciente."""

    class Meta:

        model = Paciente
        fields = (
            'nombre_paciente',
            'apellido_paciente',
            'fecha_nacimiento_paciente',
            'email_paciente',
            'telefono_paciente',
            'id_estado_civil',
            'id_sexo',
        )
        widgets = {
            'nombre_paciente' : forms.TextInput(
                attrs={'type':'text', 'class':'form-control', 'id':'nombrePaciente'}
            ),
            'apellido_paciente' : forms.TextInput(
                attrs={'type':'text', 'class':'form-control', 'id':'apellidoPaciente'}
            ),
            'fecha_nacimiento_paciente' : forms.TextInput(
                attrs={'type':'date', 'class':'form-control', 'id':'fechaNacimientoPaciente'}
            ),
            'email_paciente' : forms.TextInput(
                attrs={'type':'text', 'class':'form-control', 'id':'emailPaciente'}
            ),
            'telefono_paciente' : forms.TextInput(
                attrs={'type':'text', 'class':'form-control', 'id':'telefonoPaciente'}
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


class ReferenciaForm(forms.ModelForm):
    """Form definition for Referencia."""

    class Meta:
        """Meta definition for Referenciaform."""

        model = Referencia
        fields = (
            'nombre_referencia',
            'id_tipo_referencia',
        )
        widgets = {
            'nombre_referencia':forms.TextInput(
                attrs={'type':'text', 'class':'form-control', 'id': 'pacienteNombreReferencia'}
            ),
            'id_tipo_referencia':forms.Select(
                attrs={'class':'form-select', 'id':'pacienteTipoReferencia'}
            )
        }


class ContactoForm(forms.ModelForm):
    """Form definition for Contacto."""

    class Meta:
        """Meta definition for Contactoform."""

        model = Contacto
        fields = (
            'nombre_contacto',
            'apellido_contacto',
            'responsable_contacto',
            'telefono_contacto',
            'id_tipo_contacto',
            'id_sexo_contacto',
        )
        widgets = {
            'nombre_contacto' : forms.TextInput(
                attrs={'type':'text', 'class':'form-control', 'id': 'nombreContacto'}
            ),
            'apellido_contacto' : forms.TextInput(
                attrs={'type':'text', 'class':'form-control', 'id':'apellidoContacto'}
            ),
            'responsable_contacto' : forms.CheckboxInput(
                attrs={'type':'checkbox', 'class':'form-check-input', 'id':'responsableContacto'}
            ),
            'telefono_contacto' : forms.TextInput(
                attrs={'type':'text', 'class':'form-control', 'id':'telefonoContacto'}
            ),
            'id_sexo_contacto' : forms.Select(
                attrs={'type':'text', 'class':'form-select', 'id':'sexoContacto'}
            ),
            'id_tipo_contacto' : forms.Select(
                attrs={'type':'text', 'class':'form-select', 'id':'tipoContactoContacto'}
            ),
        }
