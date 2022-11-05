from django.forms import ModelForm
from django import forms
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'featured_image', 'description', 'demo_link', 'source_link', 'tags')
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
            'title': forms.TextInput(
                attrs={'class': 'input input--text',  'placeholder': 'Enter Your Title'}),
            'description': forms.Textarea(
                attrs={'class': 'input input--text', 'placeholder': 'Enter Your Description'}),
            'demo_link': forms.TextInput(
                attrs={'class': 'input input--text', 'placeholder': 'Enter Your Demo link'}),
            'source_link': forms.TextInput(
                attrs={'class': 'input input--text', 'placeholder': 'Enter Your Source link'}),
        }
