from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView , View
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from post.models import Comment, Post
from panel.views.posts.forms import BlogForm

class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'panel/posts/list.html'
    context_object_name = 'posts'


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'panel/posts/create.html'
    form_class = BlogForm
    success_url = reverse_lazy('post:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    template_name = 'panel/posts/create.html'
    form_class = BlogForm

    success_url = reverse_lazy('post:list')

class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post 
    template_name = 'panel/posts/detail.html'
    form_class = BlogForm
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object)
        return context

class PostDeleteView(LoginRequiredMixin,View):
    def get(self,request,pk,**kwargs):
        obj = get_object_or_404(Post,pk=pk)
        obj.delete()
        return redirect(reverse_lazy('post:list'))




class PostDashboardListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'panel/posts/dashboard.html'      
    context_object_name = 'posts'
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Annotate each post with its comments (like your DetailView)
        for post in context['posts']:
            post.comments_list = Comment.objects.filter(post=post)
        return context
