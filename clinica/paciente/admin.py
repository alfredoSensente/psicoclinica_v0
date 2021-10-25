"""Admin Paciente"""
from paciente.models import Medicamento
from paciente.models import Sexo
from paciente.models import EstadoCivil
from paciente.models import TipoContacto
from paciente.models import Departamento
from paciente.models import TipoReferencia
# Dependen de Departamento
from paciente.models import Municipio
# Dependen de Municipio
from paciente.models import Direccion
# Dependen de Sexo, Estado Civil, Direccion
from paciente.models import Paciente
# Dependen de Paciente
from paciente.models import TelefonoPaciente
from paciente.models import EmailPaciente
from paciente.models import ExpedienteClinico
# Dependen de Tipo Referencia y Paciente
from paciente.models import Referencia
# Dependen de Paciente, Tipo Contacto y Sexo
from paciente.models import Contacto
# Dependen de Contacto
from paciente.models import TelefonoContacto
# Dependen de Expediente Clinico
from paciente.models import Tratamiento
# Dependen de Expediente Clinco y Medicamento
from paciente.models import Padecimiento
# Dependen de Padecimiento
from paciente.models import TelefonoMedico

from django.contrib import admin

# Class


class PhonePatientInline(admin.StackedInline):
    """Varios pacientes"""
    model = TelefonoPaciente
    extra = 3


class PatientAdmin(admin.ModelAdmin):
    """Un paciente"""
    fieldsets = [
        (None,{
            'fields': [
                'nombre',
                'apellido',
                'id_estado_civil',
                'id_sexo',
                'id_direccion',
            ]
        }),
        ('Date information', {
            'fields': [
                'fecha_nacimiento',
                ],
            'classes': [
                'collapse'
            ]
        }),
    ]
    inlines = [PhonePatientInline]


# Register your models here.
admin.site.register(Medicamento)
admin.site.register(Sexo)
admin.site.register(EstadoCivil)
admin.site.register(TipoContacto)
admin.site.register(Departamento)
admin.site.register(TipoReferencia)
admin.site.register(Municipio)
admin.site.register(Direccion)
admin.site.register(Referencia)
admin.site.register(Paciente, PatientAdmin)
admin.site.register(TelefonoPaciente)
admin.site.register(EmailPaciente)
admin.site.register(ExpedienteClinico)
admin.site.register(Contacto)
admin.site.register(TelefonoContacto)
admin.site.register(Tratamiento)
admin.site.register(Padecimiento)
admin.site.register(TelefonoMedico)
