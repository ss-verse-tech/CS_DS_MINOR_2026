from django.shortcuts import render
from .models import Student
# Create your views here.
def Home(request):
    std_data = Student.objects.all()
    return render(request, 'index.html', {'std_data':std_data})