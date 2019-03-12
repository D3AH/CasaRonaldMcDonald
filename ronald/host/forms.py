from django import forms
from .models import House, Hospital, Guest

class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['name', 'address', 'department', 'phone_address']
