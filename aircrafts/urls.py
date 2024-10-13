from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter
from .views import AircraftViewSet

router = DefaultRouter()
router.register(r'aircrafts', AircraftViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

    path('assemble/', views.assemble_aircraft, name='assemble_aircraft'),
    path('list/', views.aircraft_list, name='aircraft_list'), 
]
