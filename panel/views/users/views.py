from django.http import request
from django.shortcuts import get_list_or_404, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, View 
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.forms import UserCreationForm


from panel.views.users.forms import UserModelForm
from post.models import Comment, Post 


User = get_user_model()

class UserProfileView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    model = User 
    template_name = 'panel/users/profile.html'
    context_object_name = 'user'
    permission_required = ['perms.auth.view_user']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(user=self.object)
        context['comments'] = Comment.objects.filter(user=self.object)
        return context


class UserListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    model = User 
    template_name = 'panel/users/list.html'
    context_object_name = 'users'
    permission_required = ['perms.auth.view_user']

class UserCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    model = User
    form_class = UserModelForm
    template_name = 'panel/users/create.html'
    success_url = reverse_lazy('users:list')
    permission_required = ['perms.auth.add_user']

class UserDeleteView(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = ['perms.auth.delete_user']
    def get(self,request,pk):
        obj = get_object_or_404(User,pk=pk)
        obj.delete()

class UserUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model = User 
    template_name = 'panel/users/create.html'
    form_class = UserModelForm
    permission_required = ['perms.auth.change_user']
    success_url = reverse_lazy('users:list')

