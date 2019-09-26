from django.conf.urls import include, url
from .views import CyclistAutocomplete, home, records, register

urlpatterns = [
    url(r'^$', home, name='home',),
    url(r'^records/$', records, name='records'),
    url(r'^cyclist-autocomplete/$', CyclistAutocomplete.as_view(), name='cyclist-autocomplete',),
    url(r'^register/$', register, name='register'),
]
