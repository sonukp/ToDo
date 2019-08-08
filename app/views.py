from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import TodoClass, STATUS_CHOICES
from .forms import ToDoClassForm
from django.shortcuts import redirect
from django.utils import timezone

# Create your views here.


# To list all the tasks in the form
def task_list(request):
    tasks = TodoClass.objects.filter(is_deleted=False)
    return render(request, 'app/task_list.html', {'tasks': tasks})


def task_detail(request, title):
    task = get_object_or_404(TodoClass, title=title)
    return render(request, 'app/task_details.html', {'task': task})


def task_new(request):
    if request.method == "POST":
        form = ToDoClassForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            # task.title = request.title
            # task.description = request.description
            # task.task_time = request.task_time
            task.save()
            return redirect('task_list')
    else:
        form = ToDoClassForm()
    return render(request, 'app/newtask.html', {'form': form})


def task_edit(request, title):
    task = get_object_or_404(TodoClass, title=title)
    if request.method == "POST":
        form = ToDoClassForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.modified = timezone.now()
            task.status = 'PEND'
            task.save()
            return redirect('task_detail', title=task.title)
    else:
        form = ToDoClassForm(instance=task)
    return render(request, 'app/newtask.html', {'form': form})


def task_remove(request, title):
    task = get_object_or_404(TodoClass, title=title)
    task.status = 'COMP'
    task.modified = timezone.now()
    task.is_deleted = True
    task.save()
    return redirect('task_list')


# API to list all the tasks
def list_all(request):
    tasks = TodoClass.objects.all()
    data = {"results": list(tasks.values('pk', 'title', 'description', 'task_time', 'created', 'status', 'modified', 'is_deleted' ))}
    return JsonResponse(data)


# API to GET the details of the task
def task(request, title):
    task = get_object_or_404(TodoClass, title=title)
    data = {"results": {
        'Title': task.title,
        "Description": task.description,
        "Date_Time": task.task_time,
        "Created on": task.created,
        "Status": task.status
    }}
    return JsonResponse(data)
