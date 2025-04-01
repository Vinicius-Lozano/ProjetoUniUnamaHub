from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Docs
from tasks.models import Task  
from .forms import DocumentForm
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from django.urls import reverse_lazy

class FileUploadView(LoginRequiredMixin, CreateView):
    model = Docs
    form_class = DocumentForm
    template_name = 'filemanager/upload.html'

    def form_valid(self, form):
        task_id = self.kwargs.get("pk")  
        task = get_object_or_404(Task, pk=task_id)
        form.instance.task = task  

        return super().form_valid(form)

    def get_success_url(self):
        
        return reverse_lazy('task-detail', kwargs={'pk': self.kwargs.get('pk')})

    
class FileListView(ListView):
    model = Docs
    template_name = 'filemanager/file_list.html'
    context_object_name = 'files'

class FileDeleteView(LoginRequiredMixin, DeleteView):
    model = Docs
    template_name = 'filemanager/file_confirm_delete.html'  
    success_url = reverse_lazy('task-detail')  

    def get_success_url(self):
        return reverse_lazy("task-detail", kwargs={"pk": self.object.task.pk})
