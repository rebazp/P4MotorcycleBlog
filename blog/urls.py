from . import views
from django.urls import path
from .views import PostListView, AddPostView, UpdatePostView, PostDetail, DeletePostView, UpdateCommentView, DeleteCommentView, custom_handler404, custom_handler500, custom_login


# Urls for the project
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('post_list/', PostListView.as_view(), name='post_list'),
    path('custom-login/', custom_login, name='custom_login'),
    path('article/edit/<int:pk>/', UpdatePostView.as_view(), name='update_post'),
    path('article/edit/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('article/edit/<int:pk>/remove', DeleteCommentView.as_view(), name='comment_delete'),
    path('article/edit/<int:pk>/update', UpdateCommentView.as_view(), name='update_comment'),
]


handler404 = custom_handler404
handler500 = custom_handler500


# The code in this file is inspired from:
# My own previous projects and knowledge
# Code Institute, I think therefore i blog project
# Youtube series Django Tutorial by [Net Ninja](https://www.youtube.com/watch?v=n-FTlQ7Djqc&list=PL4cUxeGkcC9ib4HsrXEYpQnTOTZE1x0uc&index=1&ab_channel=NetNinja)
# Youtube series Python Django Tutorial by [Corey Schafer](https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=1&ab_channel=CoreySchafer)
# Yoube Python Django Web Framework by [FreeCodeCamp](https://www.youtube.com/watch?v=F5mRW0jo-U4&ab_channel=freeCodeCamp.org)