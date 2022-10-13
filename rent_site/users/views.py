from email import message
import imp
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate,logout as auth_logout

def register(req):

    if req.method == "POST":
        form = UserRegisterForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                req, f'Account created succesfully for {username}')
            return redirect('manga-list')

    else:
        form = UserRegisterForm()
    return render(req, "users/register.html", {'form': form})


def login(req):

    if req.method=="POST":
        form=AuthenticationForm(req,data=req.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(req,user)
                messages.success(req,f'You are logged in succesfully as {username}')
                return redirect('manga-list')
            else:
                messages.error(req,"Invalid Credentials!!")
                
                return redirect('manga-list')
        else:
            messages.error(req, f"Invalid Credentials!!")
            
            return redirect('manga-list')

    else:
        form=AuthenticationForm()
        return render(req,'users/login.html',{"form":form})

def logout(req):
    auth_logout(req)
    messages.success(req,"You were succesfully logged out")
    return redirect('manga-list')