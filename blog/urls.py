from django.urls import path
from . import views

urlpatterns = [
    path('/', views.PostListView.as_view(), name = 'post_list'),
    path('/about', views.AboutView.as_view(), name = 'about'),
    path('/post/<pk>', views.PostDetailView.as_view(), name = 'post_detail'),
    path('/post/new', views.CreatePostView.as_view(), name = 'post_new'),
    path('/post/<pk>/update', views.PostUpdateView.as_view(), name = 'post_update'),
    path('/post/<pk>/delete', views.PostDeleteView.as_view(), name = 'post_delete'),
]