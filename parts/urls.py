
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_part, name='create_part'),
    path('update/<int:part_id>/', views.update_part, name='update_part'),
    path('delete/<int:part_id>/', views.delete_part, name='delete_part'),
    path('list/', views.parts_list, name='parts_list'),
]

