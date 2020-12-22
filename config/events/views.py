from django.shortcuts import render

# Create your views here.
def events_home(request):
    return render(request, 'events/index.html')

def new_event(request):
    return render(request, "events/new_event.html")

def preview_event(request):
    return render(request, "events/preview_event.html")