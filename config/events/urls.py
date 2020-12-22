
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.events_home),
    # create_account function in views will be fired when someone visits this path.
    path('new_event', views.new_event),
    path('preview_event', views.preview_event),
]
