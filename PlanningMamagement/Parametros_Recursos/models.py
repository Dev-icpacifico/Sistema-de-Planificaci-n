from django.db import models


class Recurso(models.Model):
    idrecurso = models.AutoField(primary_key=True)
    nombre_recurso = models.CharField(max_length=45, null=True)

    class Meta:
        db_table = 'recurso'
        ordering = ['nombre_recurso']

    def __str__(self):
        return self.nombre_recurso


class Empresa(models.Model):
    idempresa = models.AutoField(primary_key=True)
    nombre_empresa = models.CharField(max_length=45, null=True)

    class Meta:
        db_table = 'empresa'
        ordering = ['nombre_empresa']

    def __str__(self):
        return self.nombre_empresa


"""class HistCambios(models.Model):
    idhist_cambios = models.AutoField(primary_key=True)
    
    class Meta:
        db_table = 'recurso'
        ordering = ['nombre_recurso']"""


class Etapas(models.Model):
    idetapas = models.AutoField(primary_key=True)
    nombre_etapa = models.CharField(max_length=45, null=True)

    class Meta:
        db_table = 'etapas'
        ordering = ['nombre_etapa']

    def __str__(self):
        return self.nombre_etapa


class Supervisor(models.Model):
    idsupervisor = models.AutoField(primary_key=True)
    nombre_supervisor = models.CharField(max_length=45, null=True)

    class Meta:
        db_table = 'supervisor'
        ordering = ['nombre_supervisor']

    def __str__(self):
        return self.nombre_supervisor