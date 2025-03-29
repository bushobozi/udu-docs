from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post, NewsletterSubscription, Comment, AboutProfile, Message, Leader

# Register your models here.

@admin.register(Leader)
class LeadersAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'last_name', 'role', 'image', 'created_at', 'updated_at', 'image_preview')
    search_fields = ['first_name', 'middle_name', 'last_name', 'role']
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')
        return "No Image"
    image_preview.short_description = 'Image Preview'

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at', 'updated_at', 'featured', 'image_preview')
    search_fields = ('title', 'content', 'author__username')
    list_editable = ('featured',)  # Allow editing the 'featured' field in the list view
    prepopulated_fields = {'slug': ('title',)}  # Automatically generate slug from title
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" height="100" />')
        return "No Image"
    image_preview.short_description = 'Blog Image Preview'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'website', 'created_at', 'approved')
    list_filter = ('approved', 'created_at')
    search_fields = ('name', 'email', 'content', 'website')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
    approve_comments.short_description = "Approve selected comments"

@admin.register(NewsletterSubscription)
class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subscribed_at')
    search_fields = ['email']

@admin.register(AboutProfile)
class AboutProfile(admin.ModelAdmin):
    list_display = ('title', 'message')
    search_fields = ['title']

@admin.register(Message)
class Contact(admin.ModelAdmin):
    list_display = ('name', 'subject', 'email', 'message', 'contacted_at')
    search_fields = ['name']