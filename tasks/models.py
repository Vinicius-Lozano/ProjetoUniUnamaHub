from django.contrib.auth.models import User 
from django.db import models

# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('A', 'InProgress'),
        ('C', 'Complete'),
    ]

    title = models.CharField(max_length = 255)
    description = models.TextField()
    status = models.CharField(max_length = 1, choices = STATUS_CHOICES, default = 'P')
    created_at = models.DateTimeField(auto_now_add = True)
    due_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    collaborators = models.ManyToManyField(User, related_name="collaborating_tasks", blank=True)

    def __str__(self):
        return self.title