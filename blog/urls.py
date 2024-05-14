from . import views
from django.urls import path
from .views import PostListView, AddPostView, UpdatePostView, PostDetail, DeletePostView, UpdateCommentView


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('post_list/', PostListView.as_view(), name='post_list'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>/', UpdatePostView.as_view(), name='update_post'),
    path('article/edit/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path('article/edit/<int:pk>/update', UpdateCommentView.as_view(), name='update_comment'),
]