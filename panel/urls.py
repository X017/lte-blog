from django.urls import path , include

urlpatterns = [
    path('users/',include('panel.views.users.urls')),
    path('posts/',include('panel.views.posts.urls')),
    path('comments/',include('panel.views.comments.urls')),
]
