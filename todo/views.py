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
