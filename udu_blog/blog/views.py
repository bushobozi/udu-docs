from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Post, NewsletterSubscription, Comment, AboutProfile, Message, Leader
from .serializers import (
    PostSerializer, NewsletterSubscriptionSerializer, LeadersSerializer, 
    CommentSerializer, AboutProfileSerializer, MessageSerializer
)

class FeaturedPostView(APIView):
    def get(self, request, *args, **kwargs):
        # Get the featured post
        featured_post = Post.objects.filter(featured=True).first()
        
        if featured_post:
            serializer = PostSerializer(featured_post)
            return Response(serializer.data)
        else:
            return Response({"error": "No featured post found"}, status=404)

class AboutProfileCreateView(generics.ListCreateAPIView):
    queryset = AboutProfile.objects.all()
    serializer_class = AboutProfileSerializer

    @swagger_auto_schema(operation_description="Retrieve or create about profiles")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class LeadersView(generics.ListAPIView):
    queryset = Leader.objects.all()
    serializer_class = LeadersSerializer

    @swagger_auto_schema(operation_description="Retrieve list of leaders")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class AboutProfileView(generics.ListAPIView):
    queryset = AboutProfile.objects.all()
    serializer_class = AboutProfileSerializer
    lookup_field = 'title'

    @swagger_auto_schema(operation_description="Retrieve about profile by title")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'title'

    @swagger_auto_schema(operation_description="Retrieve or create blog posts")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'

    @swagger_auto_schema(operation_description="Retrieve, update or delete a post by slug")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @swagger_auto_schema(operation_description="Create a new comment")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class CommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer

    @swagger_auto_schema(operation_description="Retrieve list of approved comments for a post")
    def get_queryset(self):
        post_slug = self.kwargs['slug']
        return Comment.objects.filter(post__slug=post_slug, approved=True)

class NewsletterSubscriptionCreateView(generics.CreateAPIView):
    queryset = NewsletterSubscription.objects.all()
    serializer_class = NewsletterSubscriptionSerializer

    @swagger_auto_schema(operation_description="Subscribe to the newsletter")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class RelatedPostsView(APIView):
    @swagger_auto_schema(operation_description="Retrieve 4 related posts based on the given slug")
    def get(self, request, slug, *args, **kwargs):
        try:
            current_post = Post.objects.get(slug=slug)
            related_posts = Post.objects.exclude(id=current_post.id).order_by('-created_at')[:4]
            serializer = PostSerializer(related_posts, many=True)
            return Response(serializer.data)
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=404)

class CurrentPostsView(APIView):
    @swagger_auto_schema(operation_description="Retrieve the 3 most recent posts")
    def get(self, request, *args, **kwargs):
        current_posts = Post.objects.all().order_by('-created_at')[:3]
        if current_posts:
            serializer = PostSerializer(current_posts, many=True)
            return Response(serializer.data)
        return Response({"error": "No posts found"}, status=404)

class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    lookup_field = 'name'

    @swagger_auto_schema(operation_description="Create a new message")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
