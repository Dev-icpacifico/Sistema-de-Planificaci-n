from django.db import models
from Proyecto.models import *
from Procesos_Actividades.models import *
from Parametros_Recursos.models import *
from Choices.choices import *


# Create your models here.


class PlanificacionMaestra(models.Model):
    idplanificacion_maestra = models.AutoField(primary_key=True)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=45, null=True)
    fecha_inicio_estimada = models.DateTimeField(null=True)
    fecha_fin_estimada = models.DateTimeField(null=True)
    estado = models.IntegerField(null=True)

    class Meta:
        db_table = 'planificacion_maestra'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class DetallePlanMaestra(models.Model):
    iddetalle_plan_maestra = models.AutoField(primary_key=True)
    planificacion_maestra = models.ForeignKey(PlanificacionMaestra, on_delete=models.CASCADE)
    etapa = models.ForeignKey(Etapas, on_delete=models.CASCADE)
    edificacion = models.ForeignKey(Edificacion, on_delete=models.CASCADE)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    proceso_constructivo = models.ForeignKey(ProcesoConstructivo, on_delete=models.CASCADE)
    fecha_inicio_estimada = models.DateTimeField(null=True)
    fecha_fin_estimada = models.DateTimeField(null=True)

    class Meta:
        db_table = 'detalle_plan_maestra'
        # ordering = ['nombre']


class PlanificacionIntermedia(models.Model):
    idplanificacion_intermedia = models.AutoField(primary_key=True)
    planificacion_maestra = models.ForeignKey(PlanificacionMaestra, on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=45, null=True)
    fecha_inicio_estimada = models.DateTimeField(null=True)
    fecha_fin_estimada = models.DateTimeField(null=True)

    class Meta:
        db_table = 'planificacion_intermedia'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class DetallePlanIntermedia(models.Model):
    iddetalle_plan_intermedia = models.AutoField(primary_key=True)
    planificacion_intermedia = models.ForeignKey(PlanificacionIntermedia, on_delete=models.CASCADE)
    edificacion = models.ForeignKey(Edificacion, on_delete=models.CASCADE)
    ciclo = models.IntegerField(null=True)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    sub_proceso_constructivo = models.ForeignKey(SubProcesoConstructivo, on_delete=models.CASCADE)
    fecha_inicio_estimada = models.DateTimeField(null=True)
    fecha_fin_estimada = models.DateTimeField(null=True)

    class Meta:
        db_table = 'detalle_plan_intermedia'
        # ordering = ['nombre']


class PlanificacionSemanal(models.Model):
    idplanificacion_semanal = models.AutoField(primary_key=True)
    planificacion_intermedia = models.ForeignKey(PlanificacionIntermedia, on_delete=models.CASCADE, null=True)
    semana = models.IntegerField(null=True)
    fecha_inicio = models.DateTimeField(null=True)
    fecha_fin = models.DateTimeField(null=True)

    class Meta:
        db_table = 'planificacion_semanal'
        # ordering = ['nombre']

    def __str__(self):
        return f"Planificación semanal {self.idplanificacion_semanal}"


class DetallePlanSemanal(models.Model):
    iddetalle_plan_semanal = models.AutoField(primary_key=True)
    planificacion_semanal = models.ForeignKey(PlanificacionSemanal, on_delete=models.CASCADE)
    frente_trabajo = models.CharField(max_length=50, choices=FRENTES_CHOICES, default='obra_gruesa')
    tipo_actividad = models.CharField(max_length=50, choices=ACTIV_TYPE_CHOICES, default='pendiente')
    fase = models.IntegerField(null=True)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    ubicacion_piso = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE)
    actividad_pqt_trabajo = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField(null=True)
    fecha_fin = models.DateTimeField(null=True)
    lunes = models.CharField(max_length=50, choices=WORKED_DAY_CHOICES, default='pendiente')
    martes = models.CharField(max_length=50, choices=WORKED_DAY_CHOICES, default='pendiente')
    miercoles = models.CharField(max_length=50, choices=WORKED_DAY_CHOICES, default='pendiente')
    jueves = models.CharField(max_length=50, choices=WORKED_DAY_CHOICES, default='pendiente')
    viernes = models.CharField(max_length=50, choices=WORKED_DAY_CHOICES, default='pendiente')
    sabado = models.CharField(max_length=50, choices=WORKED_DAY_CHOICES, default='pendiente')
    domingo = models.CharField(max_length=50, choices=WORKED_DAY_CHOICES, default='pendiente')
    recursos = models.ManyToManyField(Recurso)  # Modificado de ForeignKey a ManyToManyField
    porcentaje_avance = models.FloatField(null=True)
    causa_no_cumplimiento = models.ForeignKey(Incidencia, on_delete=models.CASCADE)
    obervacion = models.TextField(null=True)

    class Meta:
        db_table = 'detalle_plan_semanal'
        # ordering = ['nombre']
