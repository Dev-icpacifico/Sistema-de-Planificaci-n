from django.contrib import admin
from .models import Actividad, Incidencia, ProcesoConstructivo, SubProcesoConstructivo


@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = ('idactividad', 'nombre_actividad')
    search_fields = ('nombre_actividad',)
    ordering = ('nombre_actividad',)


@admin.register(Incidencia)
class IncidenciaAdmin(admin.ModelAdmin):
    list_display = ('idincidencia', 'nombre_incidencia')
    search_fields = ('nombre_incidencia',)
    ordering = ('nombre_incidencia',)


@admin.register(ProcesoConstructivo)
class ProcesoConstructivoAdmin(admin.ModelAdmin):
    list_display = ('idproceso_constructivo', 'nombre_proceso_constructivo')
    search_fields = ('nombre_proceso_constructivo',)
    ordering = ('nombre_proceso_constructivo',)


@admin.register(SubProcesoConstructivo)
class SubProcesoConstructivoAdmin(admin.ModelAdmin):
    list_display = ('idsub_proceso_constructivo', 'nombre_sub_proceso_constructivo')
    search_fields = ('nombre_sub_proceso_constructivo',)
    ordering = ('nombre_sub_proceso_constructivo',)
