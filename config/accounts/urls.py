
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    
    path('', views.signup, name="signup"),
    # create_account function in views will be fired when someone visits this path.
    path('login', views.login, name="login"),
    
]
