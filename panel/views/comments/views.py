from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from panel.views.comments.forms import CommentsForm
from post.models import Comment 
from django.views.generic import ListView, CreateView,UpdateView,View,DetailView
from django.shortcuts import get_object_or_404, redirect


class CommentListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    model = Comment 
    template_name = 'panel/comments/list.html'
    context_object_name = 'comments'
    permission_required = ['perms.post.view_comment']

class CommentCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    model = Comment
    template_name = 'panel/comments/create.html'
    form_class = CommentsForm
    permission_required = ['perms.post.add_comment']
    success_url = reverse_lazy('comments:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CommentUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model = Comment
    template_name = 'panel/comments/update.html'
    form_class = CommentsForm
    permission_required = ['perms.post.change_comment']
    success_url = reverse_lazy('comments:list')

class CommentDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    model = Comment
    template_name = 'panel/comments/detail.html'
    form_class = CommentsForm 

    permission_required = ['perms.post.view_comment']


class CommentDeleteView(LoginRequiredMixin,PermissionRequiredMixin,View):

    permission_required = ['perms.post.delete_comment']
    def get(self,request,pk,**kwargs):
        obj = get_object_or_404(Comment,pk=pk)
        obj.delete()

        return redirect(reverse_lazy('comments:list'))
