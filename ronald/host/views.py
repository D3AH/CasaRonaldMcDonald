from django.http import HttpResponseRedirect
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import House, Hospital
from .forms import HouseForm, HospitalForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def addHouse(request):
    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/')
    else:
        form = HouseForm()
        
    return render(request, 'house/add_house.html', { 'form': form })

def listHouses(request):
    all_houses = get_list_or_404(House)

    return render(request, 'house/list_houses.html', { 'houses': all_houses })

def showHouse(request, house_id):
    house = get_object_or_404(House, pk=house_id)

    return render(request, 'house/show_house.html', { 'house': house })

def addHospital(request):
    if request.method == 'POST':
        form = HospitalForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/')
    else:
        form = HospitalForm()

    return render(request, 'hospital/add_hospital.html', {'form' : form})

def listHospitals(request):
    all_hospitals = get_list_or_404(Hospital)

    return render(request, 'hospital/list_hospitals.html', { 'hospitals' : all_hospitals})

def showHospital(request):
    hospital = get_object_or_404(Hospital, pk=hospital_id)

    return render(request, 'hospital/show_hospital.html', {'hospital' : hospital})
