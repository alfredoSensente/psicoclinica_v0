"""Admin Paciente"""
from paciente.models import Departamento
from paciente.models import Direccion
from paciente.models import EstadoCivil
from paciente.models import ExpedienteClinico
from paciente.models import Familiar
from paciente.models import Medicamento
from paciente.models import Municipio
from paciente.models import NumeroContacto
from paciente.models import Paciente
from paciente.models import Padecimiento
from paciente.models import Religion
from paciente.models import Sexo
from paciente.models import TipoFamiliar
from paciente.models import Tratamiento
from django.contrib import admin

# Register your models here.
admin.site.register(Sexo)
admin.site.register(Religion)
admin.site.register(EstadoCivil)
admin.site.register(TipoFamiliar)
admin.site.register(Departamento)
admin.site.register(Municipio)
admin.site.register(Direccion)
admin.site.register(Paciente)
admin.site.register(NumeroContacto)
admin.site.register(Familiar)
admin.site.register(ExpedienteClinico)
admin.site.register(Tratamiento)
admin.site.register(Medicamento)
admin.site.register(Padecimiento)
