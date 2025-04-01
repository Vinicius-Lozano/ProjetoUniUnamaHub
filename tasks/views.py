from django.shortcuts import redirect, render
from django.views.generic import ListView, DeleteView
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.detail import DetailView
from .models import Task
from .forms import TaskForm, TaskCollaboratorForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)  
        queryset |= Task.objects.filter(collaborators=self.request.user)  

        status = self.request.GET.get('status')  
        if status:
            queryset = queryset.filter(status=status)

        return queryset.distinct()
    

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_edit.html'
    success_url = reverse_lazy('task-list')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('task-list')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_create.html'
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        editing = self.request.GET.get('editing', 'false') == 'true'
        context['editing'] = editing
        if editing:
            context['form'] = TaskForm(instance=self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = TaskForm(request.POST, instance=self.object)
        if form.is_valid():
            form.save() 
            return redirect('task-detail', pk=self.object.pk)  
        context = self.get_context_data()
        context['form'] = form
        return render(request, self.template_name, context)

class TaskCollaboratorUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskCollaboratorForm
    template_name = 'tasks/task_collaborators.html'
    success_url = reverse_lazy('task-list')

    def get_queryset(self):
         return Task.objects.filter(user=self.request.user)
