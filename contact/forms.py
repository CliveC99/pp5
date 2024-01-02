from django import forms 
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('full_name', 'email', 'description',)
    
    def __init__(self, *args, **kwargs)
    placeholders = {
        'full_name': 'Full Name',
        'email': 'Email',
        'description': 'Description',
    }

    self.fields['full_name'].widget.attrs['autofocus'] = True