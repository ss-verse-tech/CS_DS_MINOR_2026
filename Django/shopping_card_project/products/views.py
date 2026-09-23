from django.shortcuts import render
from django.http import HttpResponse
from . import data
# Create your views here.

def product_home_page(request):
    return HttpResponse("I am calling from product page")

def product_id(request,**args):
    return HttpResponse(f"My product id is {args["id"]}")

def show_year(request, year):
    return HttpResponse(f"<h1>My year is {year}</h1>")

def product_list(request):
    class harsh:
        def __init__(self, room_mate):
            self.room_mate = room_mate
    data = {
        "name":"Harsh Ujala",
        "hobbies": ["Swimming", "Dance"],
        "age":40,
        "goal": "COO (chief opertaing officer)",
        "Harsh":harsh("Raghav"),
        "Profession": "I am professsionally learner",
        "student":["Rohit", "Mohit", "Sohan"],
    }   
    return render(request, "product_list.html", {"data":data })
    # return render(request, "product_list.html", data)
    # Data can be pass in two ways


def student_information(request):
    return render(request, "student_info.html", {"data":data})