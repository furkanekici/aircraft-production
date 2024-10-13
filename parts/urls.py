from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import PartViewSet

router = DefaultRouter()
router.register(r'parts', PartViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

    path('create/', views.create_part, name='create_part'),
    path('update/<int:part_id>/', views.update_part, name='update_part'),
    path('delete/<int:part_id>/', views.delete_part, name='delete_part'),
    path('list/', views.parts_list, name='parts_list'),
]
