from django.shortcuts import render, redirect
from .models import Event
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
@login_required(login_url="/accounts/login")
def events_home(request):
    #automatically ordering my events list from the database by date
    events = Event.objects.all().order_by('date')
    return render(request, 'events/index.html', {'events': events })
    #created dictionary to send to template

@login_required(login_url="/accounts/login")
def new_event(request):
    if request.method == 'POST':
        form = forms.NewEvent(request.POST, request.FILES)
        if form.is_valid():
            # save event to db
            #save it but don't commit to action yet
            instance = form.save(commit=False)
            # below: associating the author of the event with the user that is logged in
            instance.author = request.user
            instance.save()
            return redirect('events:list')
    else:
        form = forms.NewEvent()
    return render(request, "events/new_event.html",{'form': form })

@login_required(login_url="/accounts/login")
def preview_event(request):
    return render(request, "events/preview_event.html")

@login_required(login_url="/accounts/login")
def event_detail(request, slug):
    event = Event.objects.get(slug=slug)
    return render(request, 'events/event_detail.html', {'event': event })