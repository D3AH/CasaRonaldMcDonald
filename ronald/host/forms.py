from django import forms
from .models import House, Hospital, Guest
from django.contrib.auth.models import User

class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['name', 'address', 'department', 'phone_address', 'image']

class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ['name', 'address', 'department', 'web_page', 'phone_address', 'image']

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['first_name', 'last_name', 'department', 'date_of_birth', 'date_of_request']
