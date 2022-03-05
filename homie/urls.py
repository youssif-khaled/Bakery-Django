from django.urls import path
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns =[
path("", views.home),
path("about", views.about),
path("ouroffer", views.ouroffer),
path("contact", views.contacts)
]