from django.views.generic import DetailView 
from django.contrib.auth import get_user_model 


User = get_user_model()

class UserProfileView(DetailView):
    model = User 
    template_name = 'panel/users/profile.html'
    context_object_name = 'user'
