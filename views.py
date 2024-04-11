
from django.shortcuts import get_object_or_404, render, redirect
from django.shortcuts import render
from .models import *
from .forms import  * 

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    form = TaskForm() # from forms.py

    if request.method == 'POST':
        form = TaskForm(request.POST)# form will be a POST request
        if form.is_valid():#runs validation
            form.save()
        return redirect('/')#saves form and redirects to rendered page

    
    context = {'tasks' :tasks, 'form' :form}
    return render(request, 'todos/index.html', context)


def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'form' :form}
    return render(request, 'todos/update_task.html', context)


def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    
    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context ={'item' :item}
    return render(request, 'todos/delete.html', context)
