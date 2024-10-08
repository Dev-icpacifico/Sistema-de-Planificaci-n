from django.urls import include, path
from rest_framework import routers
from.views import *

# from .PlanningMamagement.urls import urlpatterns

routers = routers.DefaultRouter()
routers.register(r'recursos', RecursoViewSet)
routers.register(r'empresas', EmpresaViewSet)
routers.register(r'etapas', EtapaViewSet)
routers.register(r'supervisores',SupervisorViewSet)

urlpatterns =[
    path('', include(routers.urls)),
    # path('api-auth/', include('rest_framework.urls')),
]
