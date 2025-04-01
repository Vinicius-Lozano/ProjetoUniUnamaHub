from django.db import models
from tasks.models import Task  

class Docs(models.Model):
    file = models.FileField(upload_to='uploads/', blank=True, null=True)
    onedrive_link = models.URLField(blank=True, null=True)
    custom_name = models.CharField(max_length=255, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="documents")

    def __str__(self):
        return self.custom_name if self.custom_name else (self.file.name if self.file else self.onedrive_link)