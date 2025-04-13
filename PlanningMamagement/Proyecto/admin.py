from django.contrib import admin
from .models import Proyecto, Edificacion, Ubicacion, Zona


@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('idproyecto', 'nombre', 'descripcion', 'fecha_inicio', 'fecha_fin', 'estado')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('estado', 'fecha_inicio', 'fecha_fin')
    ordering = ('nombre',)
    date_hierarchy = 'fecha_inicio'


@admin.register(Edificacion)
class EdificacionAdmin(admin.ModelAdmin):
    list_display = ('idedificacion', 'nombre_edificacion')
    search_fields = ('nombre_edificacion',)
    ordering = ('nombre_edificacion',)


@admin.register(Ubicacion)
class UbicacionAdmin(admin.ModelAdmin):
    list_display = ('idubicacion', 'nombre_ubicacion')
    search_fields = ('nombre_ubicacion',)
    ordering = ('nombre_ubicacion',)


@admin.register(Zona)
class ZonaAdmin(admin.ModelAdmin):
    list_display = ('idzona', 'nombre_zona')
    search_fields = ('nombre_zona',)
    ordering = ('nombre_zona',)
