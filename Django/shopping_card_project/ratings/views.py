from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def rating(request):
    return HttpResponse("I am rating page and will show rating")
