from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('casas/agregar', views.addHouse, name='add_house'),
    path('casas', views.casas, name='casas'),
]
