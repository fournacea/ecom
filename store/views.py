from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.hashers import check_password

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from django.contrib import messages

from .models import Product
from .forms import SignUpForm


# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {"products": products})


def about(request):
    return render(request, 'about.html', {})


def login_user(request):
    if request.method == "POST":
        # print("POST Data:", request.POST)  # Debug: Print POST data
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            # print(username, password) #Debug 
            User = get_user_model()
            user = User.objects.get(username=username)  # Get the user object
            
            # Manually check password
            password_correct = check_password(password, user.password)
            # print(f"Password correct: {password_correct}") # Debug: Boolean
            
            if password_correct:
                # Explicitly specify ModelBackend
                user = authenticate(request, username=username, password=password)
                
                if user is not None:
                    # Debug: Print user and password hash
                    # print("Authenticated User:", user, user.last_login)
                    
                    if user.is_active:
                        login(request, user)
                        messages.success(request, ('You are now logged in. Welcome! 🥳'))
                        return redirect('about')
                    else:
                        messages.warning(request, ('Your account is inactive. Please contact support. 🤖'))
                        return redirect('login')
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
    logout(request)
    messages.success(request, ("You're logged out. Stop on by again now, ya hear!"))
    return redirect('home')


def register_user(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            print(username, password)

            # Log in User automatically after signup
            user = authenticate(username=username, password=password)

            if user is not None: 

                if user.is_active:
                    login(request, user)
                    messages.success(request, ('You are now logged in. Welcome! 🥳'))
                    return redirect('home')
                
                else:
                    messages.warning(request, ('Your account is inactive. Please contact support. 🤖'))
                    return redirect('login')
                
            else:
                    messages.warning(request, ('Invalid username or password. Please try again. 🤖'))

    return render(request, 'register.html', {"form": form})

