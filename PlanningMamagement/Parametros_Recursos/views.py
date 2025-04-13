from django.shortcuts import render
from rest_framework import permissions, viewsets

from .models import Recurso, Empresa, Etapas, Supervisor
from .serializers import RecursoSerializer, EmpresaSerializer, EtapaSerializer, SupervisorSerializer

# Create your views here.


class RecursoViewSet(viewsets.ModelViewSet):
    queryset = Recurso.objects.all()
    serializer_class = RecursoSerializer
    permission_classes = [permissions.AllowAny]
    # def perform_create(self, serializer):
      # serializer.save(empresa=self.request.user)


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [permissions.AllowAny]


class EtapaViewSet(viewsets.ModelViewSet):
    queryset = Etapas.objects.all()
    serializer_class = EtapaSerializer
    permission_classes = [permissions.AllowAny]


class SupervisorViewSet(viewsets.ModelViewSet):
    queryset = Supervisor.objects.all()
    serializer_class = SupervisorSerializer
    permission_classes = [permissions.AllowAny]
