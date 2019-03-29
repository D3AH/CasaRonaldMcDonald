
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('casas/agregar', views.addHouse, name='add_house'),
    path('casas', views.listHouses, name='list_houses'),
    path('casas/<int:house_id>/', views.showHouse, name='show_house'),
    path('casas/test_form', views.addHouseForm, name='house_form')
]