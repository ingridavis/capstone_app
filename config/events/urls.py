
from django.urls import path
from .views import EventListView, EventDetailView, EventCreateView, EventUpdateView, EventDeleteView
from . import views

app_name = 'events'

urlpatterns = [
   # home listing view
    path('', EventListView.as_view(), name='list'),
    
    # Create new post
    path('event/new/', EventCreateView.as_view(), name='new_event'),

    # detail 
    path('event/<int:pk>event_detail/', EventDetailView.as_view(), name='detail'),

    #update
    path('event/<int:pk>event_update/', EventUpdateView.as_view(), name='update'),
    
    #delete
    path('event/<int:pk>event_delete/', EventDeleteView.as_view(), name='delete'),
    
]
