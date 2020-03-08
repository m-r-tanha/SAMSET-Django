from django import forms
from .models import BlogComments

class BlogCommentsForm(forms.ModelForm):
    class Meta:
        model= BlogComments
        fields= ["firstname", "lastname", "email", "comment"]