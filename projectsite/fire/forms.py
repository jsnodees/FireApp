from django.forms import ModelForm
from django import forms
from .models import Incident, Locations

class IncidentForm(ModelForm):
    class Meta:
        model = Incident
        fields = "__all__"

class LocationsForm(ModelForm):
    class Meta:
        model = Locations
        fields = "__all__"