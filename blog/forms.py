from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    # Allow django to know which model should be used to create this form
    # fields = ('title', 'text') --> Fields that should be exposed
    class Meta:
        model = Post
        fields = ('title', 'text')