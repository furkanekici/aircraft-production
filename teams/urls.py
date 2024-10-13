from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeamViewSet

# Use DRF's router for the API views
router = DefaultRouter()
router.register(r'teams', TeamViewSet, basename='team')

urlpatterns = [
    # API routes
    path('api/', include(router.urls)),
]
