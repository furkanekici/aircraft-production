from django.urls import path
from . import views

urlpatterns = [
    path('assemble/', views.assemble_aircraft, name='assemble_aircraft'),
    path('list/', views.aircraft_list, name='aircraft_list'), 
]

