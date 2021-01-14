from django.contrib import admin
from .models import Event

# In the admin section we want to see the events:
admin.site.register(Event)

