from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("I am home page")
    return render(request, 'index.html')

def about(request):
    # return HttpResponse("Hello I am about")
    return render(request, 'about.html')




