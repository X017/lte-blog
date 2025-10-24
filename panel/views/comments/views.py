from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from panel.views.comments.forms import CommentsForm
from post.models import Comment 
from django.views.generic import ListView, CreateView,UpdateView,View,DetailView
from django.shortcuts import get_object_or_404, redirect


class CommentListView(LoginRequiredMixin,ListView):
    model = Comment 
    template_name = 'panel/comments/list.html'
    context_object_name = 'comments'

class CommentCreateView(LoginRequiredMixin,CreateView):
    model = Comment
    template_name = 'panel/comments/create.html'
    form_class = CommentsForm
    success_url = reverse_lazy('comments:list')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
class CommentUpdateView(LoginRequiredMixin,UpdateView):
    model = Comment
    template_name = 'panel/comments/update.html'
    form_class = CommentsForm
    success_url = reverse_lazy('comments:list')

class CommentDetailView(LoginRequiredMixin,DetailView):
    model = Comment
    template_name = 'panel/comments/detail.html'
    form_class = CommentsForm 


class CommentDeleteView(LoginRequiredMixin,View):
    def get(self,request,pk,**kwargs):
        obj = get_object_or_404(Comment,pk=pk)
        obj.delete()

        return redirect(reverse_lazy('comments:list'))
