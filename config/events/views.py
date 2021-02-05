from django.shortcuts import render, redirect, get_object_or_404
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


# User creates new event and submit goes to preview event. 
@login_required(login_url="/accounts/login")
def new_event(request):
    if request.method == 'POST':
        form = forms.NewEvent(request.POST, request.FILES)
        if form.is_valid():
            #save it but don't commit to action yet
            instance = form.save(commit=False)
            # below: associating the author of the event with the user that is logged in
            instance.author = request.user
            # intervene here for redirect to events, * NOT WORKING, so redirect to list
            instance.save()
            return redirect('events:list')
    else:
        form = forms.NewEvent()
    return render(request, "events/new_event.html",{'form': form })




@login_required(login_url="/accounts/login")
def event_detail(request, slug):
    event = Event.objects.get(slug=slug)

    return render(request, 'events/event_detail.html', {'event': event })

@login_required(login_url="/accounts/login")
def event_edit(request, id):
    
    return render(request, "events/event_edit.html")

@login_required(login_url="/accounts/login")
def event_delete(request, id):
    event = get_object_or_404(Event, id=id)
    
    if request.method == 'POST':
            event.delete()
            return redirect('events:list')
    context ={'event':event}
    return render(request, "events/event_delete.html", context)
