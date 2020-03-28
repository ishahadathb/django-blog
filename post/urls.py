from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog-home'),
    path('user/<str:username>/', views.UserBlogListView, name='user-post'),
    path('post/<int:pk>/', views.BlogDetails.as_view(), name='blog-details'),
    path('post/<int:pk>/update/', views.UpdateBlog.as_view(), name='blog-update'),
    path('post/<int:pk>/delete/', views.DeleteBlog.as_view(), name='blog-delete'),
    path('post/new/', views.CreateBlog.as_view(), name='new-post'),
    path('about/', views.about, name='blog-about'),
]
