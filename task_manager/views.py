from django.shortcuts import render, redirect, get_object_or_404
from task_manager.models import Task
from .forms import TaskForm

# Create your views here.

def task_list(req):
    return render(req, 'task_manager/task_list.twig', {'tasks': Task.objects.all()})

def create_task(req):
    if req.method == 'POST':
        form = TaskForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(req, 'task_manager/create_task.twig', {'form': form})

def update_task(req, pk):
    task = get_object_or_404(Task, pk=pk)
    if req.method == 'POST':
        form = TaskForm(req.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(req, 'task_manager/update_task.twig', {'form': form})

def delete_task(req, pk):
    task = get_object_or_404(Task, pk=pk)
    if req.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(req, 'task_manager/delete_task.twig', {'task': task})