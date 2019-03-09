from django.shortcuts import render, get_list_or_404
from .models import House

# Create your views here.
def index(request):
    return render(request, 'index.html')

def addHouse(request):
    return render(request, 'add_house.html')

def listHouses(request):
    all_houses = get_list_or_404(House)

    return render(request, 'list_houses.html', { 'houses': all_houses })