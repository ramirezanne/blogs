from django import forms
from django.db.models import fields
from django.forms.widgets import Textarea
from .models import blog

class BlogForm(forms.ModelForm):
    class Meta: 
        model = blog
        fields = "name","content","author","comment"
        widgets = {
            'content': Textarea()
        }

