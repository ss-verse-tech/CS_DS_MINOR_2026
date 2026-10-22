from django.http import HttpResponse
from django.shortcuts import render
from .sidebar_data import products
def home(request):
    # return HttpResponse("I am home page")
    return render(request, 'index.html', {"products": products.menu_data})

def about(request):
    # return HttpResponse("Hello I am about")
    return render(request, 'about.html' )
