"""Models Paciente"""
#Django
from django.db import models

# Create your models here.

class Sexo(models.Model):
    """Sexo"""
    id_sexo = models.AutoField(primary_key=True)
    sexo = models.CharField(max_length=45)

    def __str__(self):
        return self.sexo

    class Meta:
        db_table = 'sexo'


class EstadoCivil(models.Model):
    """Estado Civil"""
    id_estado_civil = models.AutoField(primary_key=True)
    estado_civil = models.CharField(max_length=45)

    def __str__(self):
        return self.estado_civil

    class Meta:
        db_table = 'estado_civil'


class TipoContacto(models.Model):
    """Tipo Contacto"""
    id_tipo_contacto = models.AutoField(primary_key=True)
    tipo_contacto = models.CharField(max_length=45)

    def __str__(self):
        return self.tipo_contacto

    class Meta:
        db_table = 'tipo_contacto'


class Departamento(models.Model):
    """Departamentos"""
    id_departamento = models.AutoField(primary_key=True)
    departamento = models.CharField(max_length=45, null=False)

    def __str__(self):
        return self.departamento

    class Meta:
        db_table = 'departamento'


class Municipio(models.Model):
    """Municipio"""
    id_municipio = models.AutoField(primary_key=True)
    municipio = models.CharField(max_length=45, null=False)
    id_departamento = models.ForeignKey(
        Departamento,
        on_delete=models.CASCADE,
        db_column='id_departamento'
    )

    def __str__(self):
        return f'{self.municipio} - {self.id_departamento}'

    class Meta:
        db_table = 'municipio'


class TipoReferencia(models.Model):
    """Tipo Referencia"""
    id_tipo_referencia = models.AutoField(primary_key=True)
    tipo_referencia = models.CharField(max_length=45)

    def __str__(self):
        return self.tipo_referencia

    class Meta:
        db_table = 'tipo_referencia'


class Direccion(models.Model):
    """Direccion"""
    id_direccion = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=255, null=False)
    id_municipio = models.ForeignKey(
        Municipio,
        on_delete=models.CASCADE,
        db_column='id_municipio'
    )

    def __str__(self):
        return self.direccion

    class Meta:
        db_table = 'direccion'


class Paciente(models.Model):
    """paciente"""
    id_paciente = models.AutoField(primary_key=True)
    nombre_paciente = models.CharField(max_length=45)
    apellido_paciente = models.CharField(max_length=45)
    fecha_nacimiento_paciente = models.DateField()
    email_paciente = models.CharField(max_length=45, null=True)
    telefono_paciente = models.CharField(max_length=45)
    id_estado_civil = models.ForeignKey(
        EstadoCivil,
        on_delete=models.CASCADE,
        db_column='id_estado_civil'
    )
    id_sexo = models.ForeignKey(
        Sexo,
        on_delete=models.CASCADE,
        db_column='id_sexo'
    )
    id_direccion = models.OneToOneField(
        Direccion,
        on_delete=models.CASCADE,
        db_column='id_direccion'
    )

    def __str__(self):
        return self.nombre_paciente + " " + self.apellido_paciente

    class Meta:
        db_table = 'paciente'


class Referencia(models.Model):
    """Referencia"""
    id_referencia = models.AutoField(primary_key=True)
    nombre_referencia = models.CharField(max_length=45)
    id_tipo_referencia = models.ForeignKey(
        TipoReferencia,
        on_delete=models.CASCADE,
        db_column='id_tipo_referencia'
    )
    id_paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE,
        db_column='id_paciente'
    )

    def __str__(self):
        return self.nombre_referencia

    class Meta:
        db_table = 'referencia'


class Contacto(models.Model):
    """Contacto"""
    id_contacto = models.AutoField(primary_key=True)
    nombre_contacto = models.CharField(max_length=45)
    apellido_contacto = models.CharField(max_length=45)
    responsable_contacto = models.BooleanField()
    telefono_contacto = models.CharField(max_length=45)
    id_paciente = models.ForeignKey(
        Paciente,
        on_delete = models.CASCADE,
        db_column = 'id_paciente'
    )
    id_tipo_contacto = models.ForeignKey(
        TipoContacto,
        on_delete = models.CASCADE,
        db_column = 'id_tipo_contacto'
    )
    id_sexo_contacto = models.ForeignKey(
        Sexo,
        on_delete=models.CASCADE,
        db_column='id_sexo'
    )

    def __str__(self):
        return self.nombre_contacto+ " " + self.apellido_contacto

    class Meta:
        db_table = 'contacto'


class ExpedienteClinico(models.Model):
    """Datos Clincos"""
    id_expediente_clinico = models.AutoField(primary_key=True)
    id_paciente = models.OneToOneField(
        Paciente,
        on_delete=models.CASCADE,
        db_column='id_paciente'
    )

    def __str__(self):
        return str(self.id_expediente_clinico)

    class Meta:
        db_table = 'datos_clinicos'


class Tratamiento(models.Model):
    """Tratamiento"""
    id_tratamiento = models.AutoField(primary_key=True)
    motivo = models.CharField(max_length=45, null=False)
    fecha_inicio = models.DateField(null=False)
    fecha_final = models.DateField(null=True)
    alta = models.BooleanField(default=False)
    descripcion = models.TextField(null=True)
    id_expediente_clinico = models.ForeignKey(
        ExpedienteClinico,
        on_delete = models.CASCADE,
        db_column = 'id_expediente_clinico'
    )

    def __str__(self):
        return f'Motivo: {self.motivo}'

    class Meta:
        db_table = 'tratamiento'


class Medicamento(models.Model):
    """Medicamentos"""
    id_medicamento = models.AutoField(primary_key=True)
    medicamento = models.CharField(max_length=45, null=False)

    def __str__(self):
        return self.medicamento

    class Meta:
        db_table = 'medicamento'


class Padecimiento(models.Model):
    """municipio"""
    id_padecimiento = models.AutoField(primary_key=True)
    padecimiento = models.CharField(max_length=45, null=False)
    nombre_medico = models.CharField(max_length=45, null=False)
    telefono_medico = models.CharField(max_length=45,null=False)
    id_medicamento = models.ForeignKey(
        Medicamento,
        on_delete=models.CASCADE,
        db_column='id_medicamento'
    )
    id_expediente_clinico = models.ForeignKey(
        ExpedienteClinico,
        on_delete=models.CASCADE,
        db_column='id_expediente_clinico'
    )

    def __str__(self):
        return self.padecimiento

    class Meta:
        db_table = 'padecimiento'
