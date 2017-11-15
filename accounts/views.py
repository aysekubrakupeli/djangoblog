from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from .forms import UserLoginForm, UserRegistrationForm


# Create your views here.
def get_index(request):
    return render(request, 'index.html')
    
@login_required(login_url='/accounts/login')
def profile(request):
    return render(request, "profile.html")
    
def logout(request):
    auth.logout(request)
    return redirect(get_index)
    
def login(request):
    if request.method=="POST":
        form=UserLoginForm(request.POST)
        
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data['username'],
                                     password=form.cleaned_data['password'])

            if user is not None:
                auth.login(request, user)
                messages.success(request, "You have successfully logged in")
                return redirect(profile)
            else:
                form.add_error(None, "Your username or password was not recognised")
    
    else:
        form = UserLoginForm()
    
    return render(request, "login.html", {'form': form})


def register(request):
    if request.method=="POST":
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            
            user = auth.authenticate(username=form.cleaned_data['username'],
                                     password=form.cleaned_data['password1'])
                                     
            if user is not None:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")
                return redirect(profile)
    else:
        form = form.add_error(None, "Your username or passwords was not recognised")
    
    return render(request, "register.html", {'form': form})
