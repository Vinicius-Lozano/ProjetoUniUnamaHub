from django import forms
from django.contrib.auth.models import User
from .models import Task
from dal import autocomplete

class TaskForm(forms.ModelForm):
    collaborators = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(
            url='user-autocomplete'
        ),
        required=False,
        label="Adicionar colaboradores"
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'due_date', 'collaborators']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'collaborators': autocomplete.ModelSelect2Multiple(
                url='user-autocomplete',
                attrs={'class': 'form-control'}
            ),
        }

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
