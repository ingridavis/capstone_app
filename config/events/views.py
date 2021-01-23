from django.shortcuts import render
from .models import Event
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/accounts/login")
def events_home(request):
    #automatically ordering my events list from the database by date
    events = Event.objects.all().order_by('date')
    return render(request, 'events/index.html', {'events': events })
    #created dictionary to send to template

@login_required(login_url="/accounts/login")
def new_event(request):
    return render(request, "events/new_event.html")

@login_required(login_url="/accounts/login")
def preview_event(request):
    return render(request, "events/preview_event.html")

@login_required(login_url="/accounts/login")
def event_detail(request, slug):
    event = Event.objects.get(slug=slug)
    return render(request, 'events/event_detail.html', {'event':event })