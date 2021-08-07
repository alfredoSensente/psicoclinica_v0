from django import forms
from django.db.models.fields import DateField, TextField
from django.forms import widgets
from django.forms.widgets import Textarea, Widget
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
        widgets = {
            'nombre':forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'apellido':forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'fecha_nacimiento' : forms.TextInput(attrs={'type':'date', 'class':'form-control'}),
            'id_religion':forms.Select(attrs={'type':'text', 'class':'form-select'}),
            'id_estado_civil':forms.Select(attrs={'type':'text', 'class':'form-select'}),
            'id_sexo':forms.Select(attrs={'type':'text', 'class':'form-select'}),
        }
