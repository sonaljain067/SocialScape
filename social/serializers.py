from rest_framework import serializers 
from .models import * 

class CreatePostSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    class Meta: 
        model = Post 
        fields = ['id', 'title','description', 'created_at']

    def create(self, validated_data):
        users_data = validated_data.pop('user', [])
        post = Post.objects.create(**validated_data)
        post.user.set(users_data)
        return post
    
    def get_created_at(self, obj):
        return obj.created_at.strftime("%Y-%m-%d %I:%M:%S %p")

class PostSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Post 
        fields = ['id', 'likes_count', 'comments_count'] 

class LikePostSerializer(serializers.ModelSerializer):
    class Meta: 
        model = LikePost
        fields = '__all__'

class CommentPostSerializer(serializers.ModelSerializer):
    class Meta: 
        model = CommentPost
        fields = '__all__'

class FollwerFollowingSerializer(serializers.ModelSerializer):
    follower = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()
    class Meta: 
        model = FollowerFollowing
        fields = ['username', 'follower', 'following']

    def get_follower(self,obj):
        return obj.follower_count 
    
    def get_following(self, obj):
        return obj.following_count


class ListCommentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentPost
        fields = ["comment"]

    def to_representation(self, instance):
        return instance.comment

class ListPostSerializer(serializers.ModelSerializer):
    comments = ListCommentPostSerializer(many= True)
    likes = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()

    class Meta: 
        model = Post 
        fields = ['id', 'title','description', 'likes', 'comments', 'created_at']

    def get_likes(self, obj):
        return obj.likes_count
    
    def get_created_at(self, obj):
        return obj.created_at.strftime("%Y-%m-%d %I:%M:%S %p")


