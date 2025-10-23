from django.forms import ModelForm, Select, Textarea

from post.models import Comment


class CommentsForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['post','content'] 
        widgets = {
            'post': Select(attrs={'class': 'form-select'}),
            "content": Textarea(attrs={'class':'form-control','placeholder':'یک کامنت بنویسید'})
        }
