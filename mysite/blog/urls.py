"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from blog import views
from django.contrib import admin

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('post_list', views.PostListView.as_view(), name='post_list'),
    path('post_<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/add', views.PostAddView.as_view(), name='post_add'),
    path('post_<int:pk>/delete', views.PostDeleteView.as_view(), name='post_delete'),
    path('post_<int:pk>/comment/add',
         views.add_comment_to_post, name='comment_add'),
    path('comment_<int:pk>/delete',
         views.CommentDeleteView.as_view(), name='comment_delete'),
    path('comment_<int:pk>', views.CommentDetailView.as_view(),
         name='comment_detail'),
    # path('post_<int:pk>/like',
    #      views.PostLikeToggleRedirect.as_view(), name='post_like'),
    path('api/post_<int:pk>/like',
         views.PostLikeToggleAPI.as_view(), name='post_like_api'),
    path('user_posts/', views.UserPostsView.as_view(), name='user_post_list'),
    path('post_search/', views.PostSearchView.as_view(), name='posts_search'),

]
