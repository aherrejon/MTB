from dal import autocomplete
from django import forms
from .models import Suscription

class SuscriptionForm(forms.ModelForm):
    
    class Meta:
        model = Suscription
        #fields = ('event',  'cyclist', 'jersey', 'medal', 'ride', 'size', 'package', 'status', 'supply')
        fields = ('event',  'cyclist', 'jersey', 'medal', 'size', 'package', 'status', 'payment')
        widgets = {
            'cyclist': autocomplete.ModelSelect2(url='cyclist-autocomplete')
        }
