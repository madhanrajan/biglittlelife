from django.shortcuts import render, redirect
from django.urls import reverse
from blog.models import Post, Comment
from django.shortcuts import get_object_or_404, redirect
from blog.forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import auth
from django.views.generic import RedirectView
from django.contrib.auth.decorators import login_required
from django.views.generic.list import MultipleObjectMixin
from django.db.models import Q
from itertools import chain
import dateparser
from django.views.generic import (
    ListView, DetailView, CreateView, DeleteView, TemplateView)
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions


# Create your views here.


class PostListView(ListView):
    template_name = 'blog/post_list.html'
    model = Post
    paginate_by = 10
    queryset = Post.objects.all().order_by('-create_date')


class PostDetailView(DetailView, MultipleObjectMixin):
    template_name = 'blog/post_detail.html'
    model = Post
    paginate_by = 1

    def get_context_data(self, **kwargs):
        object_list = self.object.sorted_comments()
        context = super().get_context_data(object_list=object_list, **kwargs)

        context["isAuthenticated"] = (
            self.object.author.id == self.request.user.id)
        return context


class PostAddView(LoginRequiredMixin, CreateView):
    template_name = 'blog/post_add.html'
    model = Post
    fields = ["post"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostAddView, self).form_valid(form)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})


class PostDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'blog/post_delete.html'
    model = Post

    def get_success_url(self):
        return reverse('post_list')


@login_required
def add_comment_to_post(request, pk):
    form = CommentForm()
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            text = form.cleaned_data['comment']
            comment = Comment()
            comment.comment = text
            comment.post = post
            comment.author = request.user
            comment.save()

            return redirect('post_detail', pk=pk)
        else:
            CommentForm()
    return render(request, 'blog/comment_add.html', {'form': form})


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment

    template_name = 'blog/comment_delete.html'

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.post.pk})


class CommentDetailView(DetailView):
    model = Comment
    template_name = 'blog/comment_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["isAuthenticated"] = (
            self.object.author.id == self.request.user.id or self.object.post.author.id == self.request.user.id)
        return context


# class PostLikeToggleRedirect(RedirectView, LoginRequiredMixin):

#     def get_redirect_url(self, *args, **kwargs):
#         obj = get_object_or_404(Post, pk=self.kwargs.get('pk'))
#         url_ = reverse('post_detail', kwargs={'pk': self.kwargs.get('pk')})
#         user = self.request.user
#         if user in obj.likes.all():
#             obj.likes.remove(user)
#         else:
#             obj.likes.add(user)

#         return url_


class PostLikeToggleAPI(APIView, LoginRequiredMixin):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk, format=None):

        obj = get_object_or_404(Post, pk=pk)
        user = self.request.user

        if user in obj.likes.all():
            obj.likes.remove(user)
            likes = obj.likes.count()

            text = "Like Post | Total: " + str(likes) + " likes"
        else:
            obj.likes.add(user)
            likes = obj.likes.count()

            text = "Unlike Post | Total: " + str(likes) + " likes"

        data = {
            "text": text,
        }

        return Response(data)


class UserPostsView(LoginRequiredMixin, ListView):
    template_name = 'blog/user_posts.html'
    model = Post
    paginate_by = 10

    def get_queryset(self):
        posts = self.request.user.posts.all().order_by('-create_date')
        return posts


class PostSearchView(ListView):
    template_name = 'blog/posts_search.html'
    model = Post
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        post_list = Post.objects.filter(Q(post__icontains=query))

        users = User.objects.filter(Q(username__icontains=query))
        for user in users:
            post_list = post_list | user.posts.all()

        try:
            post_list = post_list | Post.objects.filter(
                create_date__date=dateparser.parse(query).date())
        except:
            pass
        return post_list


class Index(TemplateView):
    template_name = 'blog/index.html'
