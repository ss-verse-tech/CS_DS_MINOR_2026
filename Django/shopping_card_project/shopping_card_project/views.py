from django.http import HttpResponse

def home(request):
    return HttpResponse("I am home page")

def about(request):
    return HttpResponse("Hello I am about")



