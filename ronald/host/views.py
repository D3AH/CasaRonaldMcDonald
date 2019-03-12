from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import House

# Create your views here.
def index(request):
    return render(request, 'index.html')

def addHouse(request):
    return render(request, 'house/add_house.html')

def listHouses(request):
    all_houses = get_list_or_404(House)

    return render(request, 'house/list_houses.html', { 'houses': all_houses })

def showHouse(request, house_id):
    house = get_object_or_404(House, pk=house_id)

    return render(request, 'house/show_house.html', { 'house': house })