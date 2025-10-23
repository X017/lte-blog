from django.urls import path 
from .views import CommentListView, CommentCreateView , CommentDetailView, CommentUpdateView , CommentDeleteView 


app_name = 'comments'
urlpatterns = [
    path('',CommentListView.as_view(),name='list'),
    path('create',CommentCreateView.as_view(),name='create'),
    path('<int:pk>/update',CommentUpdateView.as_view(),name='update'),
    path('<int:pk>/detail',CommentDetailView.as_view(),name='detail'),
    path('<int:pk>/delete',CommentDeleteView.as_view(),name='delete'),
]
