from rest_framework import serializers
from.models import Post, NewsletterSubscription, Comment, AboutProfile, Leader, Message
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']  # Include only the username (or add more fields if needed)

class LeadersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leader
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)  # include Authname
    class Meta:
        model = Post
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class NewsletterSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterSubscription
        fields = '__all__'

class AboutProfileSerializer(serializers.ModelSerializer):
    class Meta: 
        model = AboutProfile
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Message
        fields = '__all__'