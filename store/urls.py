from django.urls import path
from django.views.generic import RedirectView
from . import views


urlpatterns = [
    # Base pages
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    
    # User Login and Profile
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register-user'),
    path('update/', views.update_user, name='update-user'),
    
    # Products 
    path('product/<int:pk>', views.product, name='product'),
    path('category/<str:cat>', views.category, name='category'),
    path('category-summary/', views.category_summary, name='category-summary'),
    
    # Search Function
    path('search/', views.search, name='search'),
    
    # Favicon functionality  
    path('favicon.ico', RedirectView.as_view(url='/static/assets/favicon.ico')),
]
