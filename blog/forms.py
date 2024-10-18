from django import forms
from .models import Post  # Assuming you have a Post model defined

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']  # Add other fields as necessary
