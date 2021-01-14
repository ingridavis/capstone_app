from django.shortcuts import render
from .models import Event
from django.http import HttpResponse

# Create your views here.
def events_home(request):
    #automatically ordering my events list from the database by date
    events = Event.objects.all().order_by('date')
    return render(request, 'events/index.html', {'events': events })
    #created dictionary to send to template
def new_event(request):
    return render(request, "events/new_event.html")

def preview_event(request):
    return render(request, "events/preview_event.html")

def event_detail(request, slug):
    event = Event.objects.get(slug=slug)
    return render(request, 'events/event_detail.html', {'event':event })