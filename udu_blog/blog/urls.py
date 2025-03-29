from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostListCreateView.as_view(), name='post-list'),
    path('about/profile/create/', views.AboutProfileCreateView.as_view(), name="about-create"),
    path('about/profile/return/', views.AboutProfileView.as_view(), name='about-view'),
    path('posts/featured/', views.FeaturedPostView.as_view(), name='featured-posts'),
    path('posts/<slug:slug>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/<slug:slug>/related/', views.RelatedPostsView.as_view(), name='related-posts'),
    path('posts/<slug:slug>/comments/', views.CommentListView.as_view(), name='comment-list'),
    path('posts/<slug:slug>/comment/', views.CommentCreateView.as_view(), name='comment-create'),
    # path('posts/latest/', views.CurrentPostsView.as_view(), name="current-posts"),
    path('subscribe/', views.NewsletterSubscriptionCreateView.as_view(), name='subscribe'),
    path('contact/', views.MessageCreateView.as_view(), name='contact'),
    path('leaders/', views.LeadersView.as_view(), name='leaders'),
]
