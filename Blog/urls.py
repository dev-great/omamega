from django.urls import path
from .views import post_list, post_detail

app_name = 'Blog'

urlpatterns = [
    path('', post_list, name='post_list'),
    path('posts/<int:pk>/', post_detail, name='post_detail'),
    path('posts/tag/<str:tag>/', post_list, name='post_list_by_tag'),
    path('posts/category/<str:category>/',
         post_list, name='post_list_by_category'),
]
