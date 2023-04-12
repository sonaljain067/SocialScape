from django.db import models
from django.contrib.auth.models import User 
from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length = 60)
    description = models.CharField(max_length = 250, null = True, blank = True)
    user = models.ManyToManyField(User, related_name='posts_created',blank = True)
    likes_count = models.IntegerField(default = 0, blank = True)
    comments_count = models.IntegerField(default = 0, blank = True)
    created_at = models.DateTimeField(default = datetime.now, blank = True)

class LikePost(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

class CommentPost(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, blank = True, related_name = 'comments')
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True)
    comment = models.TextField()
    created_at = models.DateTimeField(default = datetime.now, blank = True)

class FollowerFollowing(models.Model):
    follower = models.ForeignKey(User, on_delete = models.CASCADE, related_name ="follower_user")
    following = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "following_user")