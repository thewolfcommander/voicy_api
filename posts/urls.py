from django.urls import path

from posts.views import *

urlpatterns = [
    path('feed/', ListPostAPIView.as_view()),
    path('feed/<slug:id>/', PostDetailAPIView.as_view()),
    path('create/', CreatePostAPIView.as_view()),
    path('category/create/', CreatePostCategoryAPIView.as_view()),
]