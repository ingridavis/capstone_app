from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #return HttpResponse("home")
    return render(request, "index.html")

