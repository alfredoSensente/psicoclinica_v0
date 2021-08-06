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


class Religion(models.Model):
    """Religión"""
    id_religion = models.AutoField(primary_key=True)
    religion = models.CharField(max_length=45)

    def __str__(self):
        return self.religion

    class Meta:
        db_table = 'religion'


class EstadoCivil(models.Model):
    """Estado Civil"""
    id_estado_civil = models.AutoField(primary_key=True)
    estado_civil = models.CharField(max_length=45)

    def __str__(self):
        return self.estado_civil

    class Meta:
        db_table = 'estado_civil'


class TipoFamiliar(models.Model):
    """Tipo Familiar"""
    id_tipo_familiar = models.AutoField(primary_key=True)
    tipo_familiar = models.CharField(max_length=45)

    def __str__(self):
        return self.tipo_familiar

    class Meta:
        db_table = 'tipo_familiar'


class Departamento(models.Model):
    """Departamentos"""
    id_departamento = models.AutoField(primary_key=True)
    departamento = models.CharField(max_length=45, null=False)

    def __str__(self):
        return self.departamento

    class meta:
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
        return self.municipio

    class meta:
        db_table = 'municipio'


class Paciente(models.Model):
    """paciente"""
    id_paciente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    fecha_nacimiento = models.DateField()
    id_religion = models.ForeignKey(
        Religion,
        on_delete=models.CASCADE,
        db_column='id_religion'
    )
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

    def __str__(self):
        return self.nombre + " " + self.apellido

    class Meta:
        db_table = 'paciente'


class Direccion(models.Model):
    """Direccion"""
    id_direccion = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=255, null=False)
    id_municipio = models.ForeignKey(
        Municipio,
        on_delete=models.CASCADE,
        db_column='id_municipio'
    )
    id_paciente = models.OneToOneField(
        Paciente,
        on_delete=models.CASCADE,
        db_column='id_paciente'
    )

    def __str__(self):
        return self.direccion

    class meta:
        db_table = 'direccion'


class NumeroContacto(models.Model):
    """Numero de Contacto"""
    id_numeros_de_contacto = models.AutoField(primary_key=True)
    numero_contacto = models.CharField(max_length=45)
    nombre_contacto = models.CharField(max_length=45)
    id_paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE,
        db_column='id_paciente'
    )

    def __str__(self):
        return self.numero_contacto

    class Meta:
        db_table = 'numero_contacto'


class Familiar(models.Model):
    """Familiar"""
    id_familiar = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    trato = models.TextField(max_length=1000)
    vives_con_el = models.BooleanField()
    ocupacion = models.CharField(max_length=45, blank=True, null=True)
    responsable = models.BooleanField()
    id_paciente = models.ForeignKey(
        Paciente,
        on_delete = models.CASCADE,
        db_column = 'id_paciente'
    )
    id_tipo_familiar = models.ForeignKey(
        TipoFamiliar,
        on_delete = models.CASCADE,
        db_column = 'id_tipo_familiar'
    )
    id_sexo = models.ForeignKey(
        Sexo,
        on_delete=models.CASCADE,
        db_column='id_sexo'
    )

    def __str__(self):
        return self.nombre+ " " + self.apellido

    class Meta:
        db_table = 'familiar'


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
    periodo = models.CharField(max_length=45, null=True)
    alta = models.BooleanField(default=False)
    descripcion = models.TextField(max_length=255, null=True)
    id_expediente_clinico = models.ForeignKey(
        ExpedienteClinico,
        on_delete = models.CASCADE,
        db_column = 'id_expediente_clinico'
    )

    def __str__(self):
        return f'Motivo: {self.motivo}'

    class meta:
        db_table = 'tratamiento'


class Medicamento(models.Model):
    """Medicamentos"""
    id_medicamento = models.AutoField(primary_key=True)
    medicamento = models.CharField(max_length=45, null=False)

    def __str__(self):
        return self.medicamento

    class meta:
        db_table = 'medicamento'


class Padecimiento(models.Model):
    """municipio"""
    id_padecimiento = models.AutoField(primary_key=True)
    padecimiento = models.CharField(max_length=45, null=False)
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

    class meta:
        db_table = 'padecimiento'
