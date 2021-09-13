from django.urls import path
from .views import *


urlpatterns = [
    # path('', home, name='blog-home'),
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>/', UserPostListView.as_view(template_name='blog/user_posts.html'), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(template_name='blog/post_detail.html'), name='post-detail'),
    path('post/new/', PostCreateView.as_view(template_name='blog/post_form.html'), name='post-create'),
    # path('', PostListView.as_view(), name='blog-home'),
    # path('', PostListView.as_view(), name='blog-home'),
    path('about/', about, name='blog-about'),

    path('gotopage/', gotopage, name='gotopage')
]
