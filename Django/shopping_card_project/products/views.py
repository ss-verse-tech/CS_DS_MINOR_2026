from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def product_home_page(request):
    return HttpResponse("I am calling from product page")

def product_id(request,**args):
    return HttpResponse(f"My product id is {args["id"]}")

def show_year(request, year):
    return HttpResponse(f"<h1>My year is {year}</h1>")
