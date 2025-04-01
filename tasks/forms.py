from django import forms
from django.contrib.auth.models import User
from .models import Task

class TaskForm(forms.ModelForm):
    collaborators = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Adicionar colaboradores"
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'due_date', 'collaborators']

class TaskCollaboratorForm(forms.ModelForm):
    collaborators = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Adicionar colaboradores"
    )

    class Meta:
        model = Task
        fields = ['collaborators']
