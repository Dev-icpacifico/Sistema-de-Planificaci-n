from django.contrib import admin
from .models import PlanificacionMaestra, DetallePlanMaestra, PlanificacionIntermedia, DetallePlanIntermedia, \
    PlanificacionSemanal, DetallePlanSemanal


@admin.register(PlanificacionMaestra)
class PlanificacionMaestraAdmin(admin.ModelAdmin):
    list_display = ('idplanificacion_maestra', 'nombre', 'fecha_inicio_estimada', 'fecha_fin_estimada', 'estado')
    search_fields = ('nombre',)
    ordering = ('nombre',)


@admin.register(DetallePlanMaestra)
class DetallePlanMaestraAdmin(admin.ModelAdmin):
    list_display = (
        'iddetalle_plan_maestra', 'planificacion_maestra', 'etapa', 'edificacion', 'ubicacion', 'proceso_constructivo',
        'fecha_inicio_estimada', 'fecha_fin_estimada')
    search_fields = ('planificacion_maestra__nombre',)
    ordering = ('planificacion_maestra',)


@admin.register(PlanificacionIntermedia)
class PlanificacionIntermediaAdmin(admin.ModelAdmin):
    list_display = (
        'idplanificacion_intermedia', 'nombre', 'fecha_inicio_estimada', 'fecha_fin_estimada', 'planificacion_maestra')
    search_fields = ('nombre',)
    ordering = ('nombre',)


@admin.register(DetallePlanIntermedia)
class DetallePlanIntermediaAdmin(admin.ModelAdmin):
    list_display = ('iddetalle_plan_intermedia', 'planificacion_intermedia', 'edificacion', 'ciclo', 'ubicacion',
                    'sub_proceso_constructivo', 'fecha_inicio_estimada', 'fecha_fin_estimada')
    search_fields = ('planificacion_intermedia__nombre',)
    ordering = ('planificacion_intermedia',)


@admin.register(PlanificacionSemanal)
class PlanificacionSemanalAdmin(admin.ModelAdmin):
    list_display = ('idplanificacion_semanal', 'semana')
    search_fields = ('semana',)
    ordering = ('idplanificacion_semanal',)
    fieldsets = [
        (
            'Encabezado Planificación',
            {
                "fields": [("planificacion_intermedia", "semana"),
                           ("fecha_inicio", "fecha_fin")],
            },
        ),
    ]


@admin.register(DetallePlanSemanal)
class DetallePlanSemanalAdmin(admin.ModelAdmin):
    list_display = (
        'iddetalle_plan_semanal', 'planificacion_semanal', 'actividad_pqt_trabajo', 'fecha_inicio', 'fecha_fin',
        'porcentaje_avance', 'causa_no_cumplimiento', 'obervacion')
    search_fields = ('planificacion_semanal__idplanificacion_semanal',)
    ordering = ('planificacion_semanal',)

    fieldsets = [
        (
            'Sección 1',
            {
                "fields": [("planificacion_semanal", "frente_trabajo", "tipo_actividad"),
                           ("fase", "supervisor", "empresa")],
            },
        ),
        (
            "Sección 2",
            {
                "classes": ["collapse"],
                "fields": [("ubicacion_piso", "zona", "actividad_pqt_trabajo")],
            },
        ),
        (
            "Sección 3",
            {
                "classes": ["collapse"],
                "fields": [("fecha_inicio", "fecha_fin"), ("lunes", "martes", "miercoles"),
                           ("jueves", "viernes", "sabado", "domingo")],
            },
        ),
        (
            "Sección 4",
            {
                "classes": ["collapse"],
                "fields": ["recursos", ("porcentaje_avance", "obervacion","causa_no_cumplimiento")],
            },
        ),
    ]

    # Override the form to include a multiple choice field for recursos
    filter_horizontal = ('recursos',)
