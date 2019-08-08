from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

STATUS_CHOICES = (
    ('PROGRESS', 'in_progress'),
    ('COMP', 'completed'),
    ('PEND', 'pending')
)


class TodoClass(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    task_time = models.TimeField(null=True, blank=True, default=datetime.time(00, 00))
    task_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PROGRESS')
    created = models.DateTimeField(default=datetime.datetime.now())
    modified = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
