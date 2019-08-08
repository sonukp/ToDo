from django.urls import path, re_path
from .views import list_all, task_detail, task_list, task_new, task_remove, task, task_edit


urlpatterns = [
    path('', task_list, name='task_list'),
    path('add', task_new, name='task_new'),
    path('<title>/remove/', task_remove, name='task_remove'),
    path('<title>/edit/', task_edit, name='task_edit'),
    path("<title>", task_detail, name='task_detail'),
    path("api", list_all, name="listall"),
    path("api/<title>", task, name='task'),
]
