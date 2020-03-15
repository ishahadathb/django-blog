from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', views.BlogDetails.as_view(), name='blog-details'),
    path('post/new/', views.CreateBlog.as_view(), name='new-post'),
    path('about/', views.about, name='blog-about'),
]
