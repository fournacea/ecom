from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate, 
    login, 
    logout, 
    get_user_model
)
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib import messages

from .models import Product
from .forms import SignUpForm


def home(request):
    """Render home page."""
    products = Product.objects.all()
    return render(request, 'home.html', {"products": products})


def about(request):
    """Render about page."""
    return render(request, 'about.html', {})


def login_user(request):
    """Handle user login."""
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            User = get_user_model()
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                user = None
            
            if user and check_password(password, user.password):
                user = authenticate(request, username=username, password=password)
                
                if user and user.is_active:
                    login(request, user)
                    messages.success(request, ('You are now logged in. Welcome! 🥳'))
                    return redirect('about')
                else:
                    messages.warning(request, ('Invalid username or password. Please try again. 🤖'))
                    return redirect('login')
            else:
                messages.warning(request, ('Invalid username or password. Please try again. 🤖'))
                return redirect('login')
        else:
            messages.warning(request, ('Please provide both username and password. 🤖'))
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def logout_user(request):
    """Handle user logout."""
    logout(request)
    messages.success(request, ("You're logged out. Stop on by again now, ya hear!"))
    return redirect('home')


def register_user(request):
    """Handle user registration."""
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            
            if user and user.is_active:
                login(request, user)
                messages.success(request, ('You are now logged in. Welcome! 🥳'))
                return redirect('home')
            else:
                messages.warning(request, ('Invalid username or password. Please try again. 🤖'))
    
    return render(request, 'register.html', {"form": form})


def product(request, pk):
    """Render product page."""
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {"product": product})
