from django import forms
from .models import Docs

class DocumentForm(forms.ModelForm):
    custom_name = forms.CharField(max_length=255, required=False, label="Nome Customizado", widget=forms.TextInput(attrs={'placeholder': 'Nome do arquivo'}))

    class Meta:
        model = Docs
        fields = ['file', 'onedrive_link', 'custom_name']