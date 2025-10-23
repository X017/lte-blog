from django.http import request
from django.shortcuts import get_list_or_404, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, View 
from django.contrib.auth import get_user_model

from panel.views.users.forms import UserModelForm
from post.models import Comment, Post 


User = get_user_model()

class UserProfileView(DetailView):
    model = User 
    template_name = 'panel/users/profile.html'
    context_object_name = 'user'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(user=self.object)
        context['comments'] = Comment.objects.filter(user=self.object)
        return context

class UserListView(ListView):
    model = User 
    template_name = 'panel/users/list.html'
    context_object_name = 'users'

class UserCreateView(CreateView):
    model = User 
    template_name = 'panel/users/create.html'
    form_class = UserModelForm
    success_url = reverse_lazy('users:list')

class UserDeleteView(View):
    model = User 
    def get(self,request,pk):
        obj = get_object_or_404(User,pk=pk)
        obj.delete()

class UserUpdateView(UpdateView):
    model = User 
    template_name = 'panel/users/create.html'
    form_class = UserModelForm
    success_url = reverse_lazy('users:list')
