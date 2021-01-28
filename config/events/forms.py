from django import forms
from . import models 


# Form for creating a new event using fields from models.py

class NewEvent(forms.ModelForm):
    class Meta:
        model = models.Event
        fields = ['title', 'slug', 'description', 'location', 'date', 'thumb']