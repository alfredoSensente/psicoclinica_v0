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
from paciente.models import ExpedienteClinico
# Dependen de Tipo Referencia y Paciente
from paciente.models import Referencia
# Dependen de Paciente, Tipo Contacto y Sexo
from paciente.models import Contacto
# Dependen de Expediente Clinico
from paciente.models import Tratamiento
# Dependen de Expediente Clinco y Medicamento
from paciente.models import Padecimiento

from django.contrib import admin

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
admin.site.register(Paciente)
admin.site.register(ExpedienteClinico)
admin.site.register(Contacto)
admin.site.register(Tratamiento)
admin.site.register(Padecimiento)
