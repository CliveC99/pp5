from django import forms 
from .models import JobApplication
import re


class JobForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ('full_name', 'job', 'email', 'phone_number',
                  'country', 'postcode',
                  'town_or_city', 'street_address1',
                  'street_address2', 'county',)
        widgets = {
            'phone_number': forms.TextInput(attrs={'pattern': r'^\+?[0-9]+$',
                                            'title': 'Enter a valid phone number.'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'job': 'Position',
            'email': 'Email',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postcode',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',

    }