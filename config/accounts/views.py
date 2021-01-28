from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.
def signup_view(request):
    # saving info to the database then redirecting to events/index.html
    if request.method=='POST':
        # create instance of form and pass request the post information
        form = UserCreationForm(request.POST)
        # if the information is valid, we want to save the information
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('events:list')
    # if it's a get request then send a blank form
    else:
        form= UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})
    

def login_view(request):
    if request.method =='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #retrive user then login the user
            user = form.get_user()
            login(request, user)
            # if statement for requesting a page but need to be logged in, then will redirect to requested page.
            if 'next'in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("events:list")
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:signup')