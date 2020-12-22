from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def create_account(request):
    form= UserCreationForm()
    return render(request, 'accounts/create_account.html', {'form:form'})

def login(request):
    return render(request, 'accounts/login.html')
