from django.contrib import admin
from .models import TodoClass

# Register your models here.


class ToDoClassAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description', 'task_time', 'task_date', 'created', 'status', 'modified', 'is_deleted')
    list_filter = ('task_time', 'task_date', 'created', 'status', 'is_deleted')
    search_fields = ('title', 'description')
    actions = ['download_csv']

    def download_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse
        # from io import StringIO
        import io

        f = io.StringIO()
        writer = csv.writer(f)
        writer.writerow(['pk', 'title', 'description', 'task_time', 'task_date', 'created', 'status', 'modified', 'is_deleted'])
        for s in queryset:
            writer.writerow([s.title, s.description, s.task_date, s.task_time, s.created, s.status, s.modified, s.is_deleted])

        f.seek(0)
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=todo-list.csv'
        return response

    download_csv.short_description = "Selected list to download CSV file."


admin.site.register(TodoClass, ToDoClassAdmin)
