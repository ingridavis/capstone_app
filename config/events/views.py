from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from . import forms




class EventListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'events/index.html'
    context_object_name = 'events'
    events = Event.objects.all().order_by('date')

class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event
    
    
class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['title', 
        'location', 
        'date', 
        'category', 
        'description', 
        'photo',]
    
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    fields = ['title', 
        'location', 
        'date', 
        'category', 
        'description', 
        'photo',]
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        event = self.get_object()
        if self.request.user == event.author:
            return True
        return False

class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    success_url = '/' # this may not work, see 46:30 min
    def test_func(self):
        event = self.get_object()
        if self.request.user == event.author:
            return True
        return False

