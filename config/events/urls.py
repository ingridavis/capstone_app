
from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    
    path('', views.events_home, name='list'),
    # create_account function in views will be fired when someone visits this path.
    path('new_event', views.new_event),
    path('preview_event', views.preview_event),
    path('<slug:slug>/', views.event_detail, name='detail'),
]
