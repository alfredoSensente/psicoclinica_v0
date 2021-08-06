from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    """Form definition for Paciente."""

    class Meta:
        """Meta definition for Pacienteform."""

        model = Paciente
        fields = (
            'nombre',
            'apellido',
            'fecha_nacimiento',
            'id_religion',
            'id_estado_civil',
            'id_sexo',
        )
