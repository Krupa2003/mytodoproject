
# Create your views here.
from django.shortcuts import render, redirect
from .models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request, 'my_tasks/index.html', {'tasks': tasks})

def create_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        Task.objects.create(title=title)
        return redirect('index')
    return render(request, 'my_tasks/create_task.html')
    
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('index')
