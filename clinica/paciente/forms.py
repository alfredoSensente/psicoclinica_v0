"""Forms Paciente"""
#Django
from django import forms

#Models
from .models import Paciente
from .models import Direccion
from .models import TelefonoPaciente
from .models import EmailPaciente
from .models import Referencia
from .models import Contacto
from .models import TelefonoContacto

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
            'telefono_paciente',
        )
        widgets = {
            'telefono_paciente' : forms.TextInput(
                attrs={'type':'number', 'class':'form-control', 'id':'telefonoTelefonoPaciente'}
            )
        }

class EmailPacienteForm(forms.ModelForm):
    """Form definition for EmailPaciente."""

    class Meta:
        """Meta definition for EmailPacienteform."""

        model = EmailPaciente
        fields = (
            'email_paciente',
        )
        widgets = {
            'email_paciente': forms.TextInput(
                attrs={'type':'email', 'class': 'form-control', 'id' : 'emailEmailpaciente'}
            )
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
            'id_sexo_contacto' : forms.Select(
                attrs={'type':'text', 'class':'form-select', 'id':'sexoContacto'}
            ),
            'id_tipo_contacto' : forms.Select(
                attrs={'type':'text', 'class':'form-select', 'id':'tipoContactoContacto'}
            ),
        }

class TelefonoContactoForm(forms.ModelForm):
    """Form definition for TelefonoContacto."""

    class Meta:
        """Meta definition for TelefonoContactoform."""

        model = TelefonoContacto
        fields = (
            'telefono_contacto',
        )
        widgets = {
            'telefono_contacto' : forms.TextInput(
                attrs={'type':'number', 'class':'form-control', 'id':'telefonoTelefonoContacto'}
            )
        }
