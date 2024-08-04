from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import (
    authenticate, 
    login, 
    logout, 
    get_user_model
)
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django import forms
from django.contrib import messages
from django.db.models import Q

from .models import Product, Category
from .forms import SignUpForm, UpdateUserForm


def home(request):
    """Render home page."""
    products = Product.objects.all()
    return render(request, 'home.html', {"products": products})


def about(request):
    """Render about page."""
    return render(request, 'about.html', {})


def search(request):
    """Search functionality."""
    if request.method == "GET":
        searched = request.GET.get('searched')
        if searched:
            print(1,searched)
        
            searched =  Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))
            print(2,searched)
        #products = Product.objects.filter()
        return render(request, 'search.html', {"searched": searched})
    return render(request, 'search.html', {})


def category(request, cat):
    """Refine items to a category"""
    # Replace hyphens with spaces
    cat = cat.replace('-', ' ').title()
    print(f"cat after .replace: {cat}")

    # Get the category from the URL
    try:
        #Look up category in database
        category =  Category.objects.get(name=cat)# Name collison possible - change soon
        products =  Product.objects.filter(category=category)
        return render(request, 'category.html', {"category": category,"products":products})
    except:
       messages.error(request, ("That category doesn't exist")) 
       return redirect('home')
   
   
def category_summary(request):
    """Display a list of all Categories"""
    categories = Category.objects.all()
    context = {"categories":categories}
    return render(request, 'category-summary.html', context)




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


def update_user(request):
    """Handle upadting user."""

    if request.user.is_authenticated:
        current_user = User.objects.get(pk=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)
        
        if user_form.is_valid():
            user_form.save()
            
            login(request, current_user)
            messages.success(request, 'Profile successfully updated!')
            return redirect('home')
        return render(request, 'update-user.html', {"user_form": user_form})
    else:
        messages.warning(request, 'You must be logged in to do that!')  
        return render(request, 'update-user.html', {})


def product(request, pk):
    """Render product page."""
    #product = Product.objects.get(id=pk)
    product = get_object_or_404(Product, id=pk)
    return render(request, 'product.html', {"product": product})
