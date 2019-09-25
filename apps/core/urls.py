from django.conf.urls import include, url
from .views import CyclistAutocomplete, home, records

urlpatterns = [
    url(
        r'^cyclist-autocomplete/$', CyclistAutocomplete.as_view(), name='cyclist-autocomplete',
    ),
    url(r'^records/$', records, name='records'),
    url(
        r'^$', home, name='home',
    ),
]
