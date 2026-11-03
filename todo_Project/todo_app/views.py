from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import todo_table
# Create your views here.
def home(request):
    data = todo_table.objects.all()
    return render(request, 'home.html', {'data': data})


def add_task(request):
    if request.method=="POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        todo_table.objects.create(title = title, description=description)
        return redirect('home')
    return render(request, 'add_task.html')


def edit_task(request,id):
    task_data = todo_table.objects.get(id = id)
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')

        if title and description:
            task_data.title = title
            task_data.description = description
            task_data.save()
            return redirect('home')
    return render(request, 'edit_task.html',{'task_data': task_data})

def delete_task(request, id):
    task_data = todo_table.objects.get(id = id)
    task_data.delete()
    return redirect('home')








