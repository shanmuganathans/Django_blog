from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
from .forms import LoginForm, RegisterForm

# Create your views here.

def sign_in(request):
    
    if request.method == "GET":
        form = LoginForm()
        return render(request, "users/login.html", {"form": form})
    elif request.method =="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username)
            user = authenticate(request, username = username, password = password)
            if user:
                login(request, user)
                messages.success(request, "Login completed")
                return redirect("posts")
    messages.error(request, "Invalid username/password")
    return render(request, "users/login.html", {"form": form})

def sign_out(request):
    logout(request)
    messages.success(request, "Yor're account have been logged out..!")
    return redirect("login")


def sign_up(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "users/register.html",{"form": form})
    elif request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "You have registered successfully..!")
            login(request, user)
            return redirect("posts")
        else:
            return render(request, "users/register.html",{"form": form})
            
        