from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import * 

urlpatterns = [
    path('authenticate/',TokenObtainPairView.as_view()),
    path(r'follow/<int:id>', FollowUserView.as_view()),
    path(r'unfollow/<int:id>',UnfollowUserView.as_view()),
    path('user', UserFollowerFollowingView.as_view()),
    path('posts/', CreatePostView.as_view()),
    path(r'posts/<int:id>', DeletePostView.as_view()),
    path(r'like/<int:id>', LikePostView.as_view()),
    path(r'unlike/<int:id>', UnlikePostView.as_view()),
    path(r'comment/<int:id>', CommentPostView.as_view()),
    path(r'posts/<int:id>/', PostView.as_view()),
    path('all_posts', AllPostsView.as_view())
]
