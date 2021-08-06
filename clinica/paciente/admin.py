from paciente.models import Departamento, Direccion, EstadoCivil, ExpedienteClinico, Familiar, Medicamento, Municipio, NumeroContacto, Paciente, Padecimiento, Religion, Sexo, TipoFamiliar, Tratamiento
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
