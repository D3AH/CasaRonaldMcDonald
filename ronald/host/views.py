from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def addHouse(request):
    return render(request, 'add_house.html')

def casas(request):
    return render(request, 'casas.html')
