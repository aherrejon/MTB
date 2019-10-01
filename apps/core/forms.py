from dal import autocomplete
from django import forms
from .models import Suscription

class SuscriptionForm(forms.ModelForm):
    
    class Meta:
        model = Suscription
        fields = ('event',  'cyclist', 'jersey', 'medal', 'size', 'package_type', 'status', 'payment')
        widgets = {
            'cyclist': autocomplete.ModelSelect2(url='cyclist-autocomplete')
        }
