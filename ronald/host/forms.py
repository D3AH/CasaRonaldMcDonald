from django import forms
from .models import House, Hospital, Guest
from django.contrib.auth.models import User

class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['name', 'address', 'department', 'phone_address']
