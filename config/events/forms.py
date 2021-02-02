from django import forms
from . import models 


# Form for creating a new event using fields from models.py

class NewEvent(forms.ModelForm):
    class Meta:
        model = models.Event
        fields = ['title', 'slug', 'location', 'date', 'category', 'description', 'thumb', ]