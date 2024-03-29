
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('casa/agregar', views.addHouse, name='add_house'),
    path('house', views.listHouses, name='list_houses'),
    path('casa/<int:house_id>/', views.showHouse, name='show_house'),
    path('hospital/agregar', views.addHospital, name='add_hospital'),
    path('hospital', views.listHospitals, name='list_hospitals'),
    path('hospital/<int:hospital_id>/', views.showHospital, name='show_hospital'),
    path('guest/agregar', views.addGuest, name='add_guest'),
    path('guest', views.listGuests, name='list_guests'),
    path('guest/<int:guest_id>/', views.showGuest, name='show_guest'),
]