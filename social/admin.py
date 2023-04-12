from django.contrib import admin
from .models import * 

admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(CommentPost)
admin.site.register(FollowerFollowing)