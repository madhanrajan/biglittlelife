from django.db import models
from .validators import validate_profane
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    post = models.TextField(max_length=200, validators=[validate_profane])
    create_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, related_name='posts')
    likes = models.ManyToManyField(
        'auth.User', related_name='post_likes', blank=True)

    def __str__(self):
        return self.post

    def sorted_comments(self):
        return self.comments.all().order_by('-create_date')

    def get_api_like_url(self):
        return reverse('post_like_api', kwargs={'pk': self.pk})


class Comment(models.Model):
    comment = models.TextField(
        max_length=200)

    author = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, related_name='comments')

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    create_date = models.DateTimeField(auto_now_add=True)

    def has_delete_permission(self, request):
        return request.user.id == self.author.id | request.user.id == self.post.author.id

    def __str__(self):
        return self.comment
