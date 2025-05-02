from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),  # This line needs the about() function to exist in views.py
    path('contact/', views.contact, name='contact'),  # Add this line for the contact page
    path('projects/', views.projects, name='projects'),  # Add this line for the projects page
]
