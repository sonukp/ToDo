from django import forms

from .models import TodoClass


class ToDoClassForm(forms.ModelForm):

    class Meta:
        model = TodoClass
        fields = ('title', 'description', 'task_time', 'task_date')
        widgets = {
            'task_date': forms.DateInput(attrs={'type': 'date'}),
            'task_time': forms.TimeInput(attrs={'type': 'time', 'format':'%H:%M'})
        }
