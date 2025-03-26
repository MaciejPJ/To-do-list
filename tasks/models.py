from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.conf import settings
from django.urls import reverse



class Task(models.Model):
    """
    Model representing a task in the system.
    """
    URGENT = 1
    MEDIUM = 2
    LOW = 3
    PRIORITY_CHOICES = [
        (URGENT, 'Highest priority'),
        (MEDIUM, 'Medium priority'),
        (LOW, 'Lowest priority')
    ]
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=MEDIUM)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(default=timezone.now() + timezone.timedelta(days=1))

    def __str__(self):
        return f'{self.title}, {self.get_priority_display()}'

    def get_absolute_url(self):
        return reverse("task_detail", kwargs={"pk": self.pk})
    
    def clean(self):
        if self.due_date < timezone.now():
            raise ValidationError("Due date cannot be in the past.")
