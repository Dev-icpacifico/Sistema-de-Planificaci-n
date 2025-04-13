from django.contrib import admin
from .models import Recurso, Empresa, Etapas, Supervisor

@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ('idrecurso', 'nombre_recurso')
    search_fields = ('nombre_recurso',)
    ordering = ('nombre_recurso',)


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('idempresa', 'nombre_empresa')
    search_fields = ('nombre_empresa',)
    ordering = ('nombre_empresa',)


@admin.register(Etapas)
class EtapasAdmin(admin.ModelAdmin):
    list_display = ('idetapas', 'nombre_etapa')
    search_fields = ('nombre_etapa',)
    ordering = ('nombre_etapa',)


@admin.register(Supervisor)
class SupervisorAdmin(admin.ModelAdmin):
    list_display = ('idsupervisor', 'nombre_supervisor')
    search_fields = ('nombre_supervisor',)
    ordering = ('nombre_supervisor',)
