from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .models import * 
from .serializers import * 

# Follow User 
class FollowUserView(CreateAPIView):
    # permission_classes = (IsAuthenticated)
    def post(self, request, id):
        try:
            user_to_follow = User.objects.get(id = id)
        except User.DoesNotExist:
            return Response({'error': 'User doesn\'t exist'}, status = status.HTTP_400_BAD_REQUEST)
        except Exception as e: 
            return Response({'error': str(e)}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        user = request.user 

        if user == user_to_follow:
            return Response({'error': 'Cannot follow yourself'})
        
        if FollowerFollowing.objects.filter(follower = user, following = user_to_follow).exists():
             return Response({'message': 'You are already following this user'}, status = status.HTTP_400_BAD_REQUEST)
        
        follow = FollowerFollowing(follower = user, following = user_to_follow)
        follow.save()

        return Response({'message': 'You are now following this user'}, status = status.HTTP_201_CREATED)
    
# Unfollow User 
class UnfollowUserView(APIView):
    def post(self, request, id):
        try:
            following_user = User.objects.get(id = id)
            user = request.user
            following_follower = FollowerFollowing.objects.get(follower = user, following = following_user)
            following_follower.delete()
            return Response({'message': f'{following_user} successfully unfollowed'}, status = status.HTTP_204_NO_CONTENT)
        
        except User.DoesNotExist:
            return Response({'error': 'User doesn\'t exist'}, status = status.HTTP_400_BAD_REQUEST)
        except FollowerFollowing.DoesNotExist:
            return Response({'error': 'You\'re not following this user'}, status = status.HTTP_400_BAD_REQUEST)
        except Exception as e: 
            return Response({'error': str(e)}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

# User's Follower Following 
class UserFollowerFollowingView(ListAPIView):
    def get(self, request):
        user = request.user 
        
        follower_count = FollowerFollowing.objects.filter(following = user).count()
        following_count = FollowerFollowing.objects.filter(follower = user).count()

        return Response({
            'username': user.username,
            'follower': follower_count,
            'following': following_count
        }, status = status.HTTP_200_OK)

# Create Post
class CreatePostView(CreateAPIView):
    serializer_class = CreatePostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=[self.request.user])

# Delete Post
class DeletePostView(DestroyAPIView):
    def delete(self, request, id): 
        post = get_object_or_404(Post, id = id, user = request.user)
        post.delete()
        return Response({'message': 'Post successfully deleted!'}, status = status.HTTP_204_NO_CONTENT)

# Like Post 
class LikePostView(APIView):
    def post(self, request, id):
        try: 
            post = Post.objects.get(id = id)
        except Post.DoesNotExist:
            return Response({'message': 'Post doesn\'t exist'}, status = status.HTTP_400_BAD_REQUEST)
       
        like_post = LikePost.objects.filter(post = post, user = request.user)
        if like_post.first(): 
            return Response({'message': 'Post was already liked'}, status = status.HTTP_200_OK)
        else:
            LikePost.objects.create(post = post, user = request.user)
            post.likes_count += 1 
            post.save()
            return Response({'message': 'Post liked successfully'}, status = status.HTTP_200_OK)
            
# Like Post 
class UnlikePostView(APIView):
    def post(self, request, id):
        try: 
            post = Post.objects.get(id = id)
        except Post.DoesNotExist:
            return Response({'message': 'Post doesn\'t exist'}, status = status.HTTP_400_BAD_REQUEST)
        
        like, created = LikePost.objects.get_or_create(post = post, user = request.user)
        if like: 
            like.delete()
            if  post.likes_count > 0:
                post.likes_count -= 1 
                post.save()
            return Response({'message': 'Post unliked succesfully'}, status = status.HTTP_200_OK)
        else:
            return Response({'message': 'Post was already unliked'}, status = status.HTTP_200_OK)
        
# Comment Post 
class CommentPostView(CreateAPIView):
    serializer_class = CommentPostSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        post = Post.objects.get(id = self.kwargs.get('id'))

        serializer = self.serializer_class(data = self.request.data)
        if serializer.is_valid():   
            serializer.save(user = self.request.user, post = post)

        post.comments_count += 1
        post.save()

        return Response({"comment_id": serializer.instance.id}, status = status.HTTP_200_OK)


# Post 
class PostView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, )
    queryset = Post.objects.all()

    def get(self, request, id):
        try:
            post = Post.objects.get(id = id)
        except: 
            return Response({'message': 'Post doesn\'t exist'}, status = status.HTTP_404_NOT_FOUND)
        return Response(PostSerializer(post).data)

# All Posts 
class AllPostsView(ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ListPostSerializer

    def get_queryset(self):
        queryset = Post.objects.filter(user = self.request.user).order_by("-created_at")
        return queryset