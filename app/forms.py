from .models import Post
from django import forms

class BlogPostForm(forms.ModelForm):

     class Meta():
        model = Post
        fields = ('title', 'content', 'complete')
