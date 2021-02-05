
from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    
    path('', views.events_home, name='list'),
    # create_account function in views will be fired when someone visits this path.
    path('new_event/', views.new_event, name="new_event"),
    path('event/<int:id>event_edit/', views.event_edit, name="edit"),
    path('event/<int:id>event_delete/', views.event_delete, name="delete"),
    path('<slug:slug>/', views.event_detail, name='detail'),
    
    
]
