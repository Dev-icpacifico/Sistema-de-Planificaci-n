from django.db import models


# Create your models here.
class Proyecto(models.Model):
    idproyecto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, null=True)
    descripcion = models.CharField(max_length=45, null=True)
    fecha_inicio = models.DateTimeField(null=True)
    fecha_fin = models.DateTimeField(null=True)
    estado = models.IntegerField(null=True)

    class Meta:
        db_table = 'proyecto'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Edificacion(models.Model):
    idedificacion = models.AutoField(primary_key=True)
    nombre_edificacion = models.CharField(max_length=45, null=True)

    class Meta:
        db_table = 'edificacion'
        ordering = ['nombre_edificacion']

    def __str__(self):
        return self.nombre_edificacion


class Ubicacion(models.Model):
    idubicacion = models.AutoField(primary_key=True)
    nombre_ubicacion = models.CharField(max_length=45, null=True)

    class Meta:
        db_table = 'ubicacion'
        ordering = ['nombre_ubicacion']

    def __str__(self):
        return self.nombre_ubicacion


class Zona(models.Model):
    idzona = models.AutoField(primary_key=True)
    nombre_zona = models.CharField(max_length=45, null=True)

    class Meta:
        db_table = 'zona'
        ordering = ['nombre_zona']

    def __str__(self):
        return self.nombre_zona