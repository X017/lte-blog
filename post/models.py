from django.db import models
from django.contrib.auth import get_user_model 

User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)
    content = models.TextField() 

    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True) 
    created_at = models.DateTimeField(auto_now_add=True) 


class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

    content = models.TextField() 
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True) 
    created_at = models.DateTimeField(auto_now_add=True) 
