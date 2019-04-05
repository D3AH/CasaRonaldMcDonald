from django.http import HttpResponseRedirect
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import House, Hospital, Guest
from .forms import HouseForm, HospitalForm, GuestForm

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
        
    return render(request, 'components/bootstrap_form.html', {'form' : form, 'action': '/casa/agregar' })

def listHouses(request):
    all_houses = get_list_or_404(House)

    return render(request, 'components/list_simple.html', { 'objects': all_houses, 'url': 'casa'})

def showHouse(request, house_id):
    house = get_object_or_404(House, pk=house_id)

    return render(request, 'show_simple.html', { 'object': house })

def addHospital(request):
    if request.method == 'POST':
        form = HospitalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/')
    else:
        form = HospitalForm()

    return render(request, 'components/bootstrap_form.html', {'form' : form, 'action': '/hospital/agregar' })

def listHospitals(request):
    all_hospitals = get_list_or_404(Hospital)

    return render(request, 'components/list_simple.html', { 'objects' : all_hospitals, 'url': 'hospital'})

def showHospital(request, hospital_id):
    hospital = get_object_or_404(Hospital, pk=hospital_id)

    return render(request, 'show_simple.html', {'object' : hospital})

def addGuest(request):
    if request.method == 'POST':
        form = GuestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/')
    else:
        form = GuestForm()

    return render(request, 'components/bootstrap_form.html', {'form' : form, 'action': '/guest/agregar'})

def listGuests(request):
    all_guests = get_list_or_404(Guest)

    return render(request, 'components/list_simple.html', { 'objects' : all_guests, 'url': 'guest'})

def showGuest(request, guest_id):
    guest = get_object_or_404(Guest, pk=guest_id)

    return render(request, 'show_simple.html', {'object' : guest})
