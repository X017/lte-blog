from django import forms

from post.models import Post


class BlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','is_active']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
