from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def product_home_page(request):
    return HttpResponse("I am calling from product page")

def product_id(request, id):
    return HttpResponse(f"My product id is {id}")
