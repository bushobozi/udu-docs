from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

# Party Leaders
# Create Leaders
class Leader(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # other_name = models.CharField(max_length=100, null=True)
    role = models.CharField(max_length=250)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)  # Add this line
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return self.role

# UDU Blog Posts
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)  # Add this line
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', default=1)  # Add this line

    def save(self, *args, **kwargs):  # Ensure the method signature is correct
        if not self.slug:
            self.slug = slugify(self.title)
        
        # Ensure only one post is featured at a time
        if self.featured:
            # Unfeature all other posts
            Post.objects.filter(featured=True).exclude(id=self.id).update(featured=False)
        
        super().save(*args, **kwargs)  # Pass *args and **kwargs to the parent class's save method

    def __str__(self):
        return self.title

# Comments to a post
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    # website = models.TextField()
    website = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)  # Admin can approve comments

    def __str__(self):
        return f"Comment by {self.name} on {self.post.title}"

# UDU Newsletter subscriptions
class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    

# About Profile
class AboutProfile(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.title
    
class Message(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=500)
    email = models.EmailField()
    message = models.TextField()
    contacted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"