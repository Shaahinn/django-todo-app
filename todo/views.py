from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:  # avoid saving empty tasks
            Task.objects.create(title=title)
        return redirect('/')  # after saving, reload the page

    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    return redirect('/')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('/')
