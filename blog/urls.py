from django.urls import path
from .views import post_list, post_detail, post_create, post_edit, post_delete  # Import the edit view

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/create/', post_create, name='post_create'),
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),  # Add this line
    path('post/<int:pk>/delete/', post_delete, name='post_delete'),
]
