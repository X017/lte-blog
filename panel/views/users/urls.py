from django.urls import path
from .views import  UserCreateView, UserDeleteView, UserListView, UserProfileView, UserUpdateView 

app_name = 'users'
urlpatterns = [
    path('', UserListView.as_view(), name='list'),
    path('<int:pk>/', UserProfileView.as_view(), name='detail'),
    path('create/', UserCreateView.as_view(), name='create'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='delete'),
]
