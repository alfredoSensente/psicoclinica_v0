"""Forms Paciente"""
from django import forms
from .models import Paciente

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
            'id_direccion',
        )
        widgets = {
            'nombre':forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'apellido':forms.TextInput(attrs={'type':'text', 'class':'form-control'}),
            'fecha_nacimiento' : forms.TextInput(attrs={'type':'date', 'class':'form-control'}),
            'id_estado_civil':forms.Select(attrs={'type':'text', 'class':'form-select'}),
            'id_sexo':forms.Select(attrs={'type':'text', 'class':'form-select'}),
            'id_direccion':forms.Select(attrs={'type':'text', 'class':'form-select'}),
        }
