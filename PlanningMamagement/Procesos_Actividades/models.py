from django.db import models


# Create your models here.

class Actividad(models.Model):
    idactividad = models.AutoField(primary_key=True)
    nombre_actividad = models.CharField(max_length=45, null=True)

    class Meta:
        db_table = 'actividad'
        ordering = ['nombre_actividad']

    def __str__(self):
        return str(self.nombre_actividad)


class Incidencia(models.Model):
    idincidencia = models.AutoField(primary_key=True)
    nombre_incidencia = models.CharField(max_length=45, null=True)

    class Meta:
        db_table = 'incidencia'
        ordering = ['nombre_incidencia']

    def __str__(self):
        return str(self.nombre_incidencia)


class ProcesoConstructivo(models.Model):
    idproceso_constructivo = models.AutoField(primary_key=True)
    nombre_proceso_constructivo = models.CharField(max_length=45, null=True)

    class Meta:
        db_table = 'proceso_constructivo'
        ordering = ['nombre_proceso_constructivo']

    def __str__(self):
        return str(self.nombre_proceso_constructivo)


class SubProcesoConstructivo(models.Model):
    idsub_proceso_constructivo = models.AutoField(primary_key=True)
    nombre_sub_proceso_constructivo = models.CharField(max_length=45, null=True)

    class Meta:
        db_table = 'sub_proceso_constructivo'
        ordering = ['nombre_sub_proceso_constructivo']

    def __str__(self):
        return str(self.nombre_sub_proceso_constructivo)
