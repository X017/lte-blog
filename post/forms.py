from django import forms

from post.models import Post


class BlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content','is_active']
