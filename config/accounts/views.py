from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def signup(request):
    # saving info to the database then redirecting to events/index.html
    if request.method=='POST':
        # create instance of form and pass request the post information
        form = UserCreationForm(request.POST)
        # if the information is valid, we want to save the information
        if form.is_valid():
            form.save()
            #later: log user in here 
            return redirect('events:list')
    # if it's a get request then send a blank form
    else:
        form= UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})
    

def login(request):
    if request.method =='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #login the user
            return redirect("events:list")
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})
