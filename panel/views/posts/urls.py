from .views import PostCreateView, PostDeleteView, PostDetailView, PostUpdateView, PostListView
from django.urls import path 


app_name = 'post'
urlpatterns = [
    path('',PostListView.as_view(),name='list'),
    path('create',PostCreateView.as_view(),name='create'),
    path('<int:pk>/update',PostUpdateView.as_view(),name='update'),
    path('<int:pk>/detail',PostDetailView.as_view(),name='detail'),
    path('<int:pk>/delete',PostDeleteView.as_view(),name='delete'),
]
