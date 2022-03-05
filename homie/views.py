from django.shortcuts import render
from django.http import response
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls.base import reverse
# from django.urls import reverse

# Create your views here.
def home(request):
    return render(request,"index.html")
   
def about(request):
    return render(request,"about.html")

def ouroffer(request):
    return render(request,"ouroffer.html")

def contacts(request):
    return render(request,"contact.html")