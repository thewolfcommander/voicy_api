from rest_framework import generics

from posts.serializers import *
from posts.models import *


class ListPostAPIView(generics.ListAPIView):
    serializer_class = PostShowSerializer
    queryset = Post.objects.all()

class CreatePostAPIView(generics.CreateAPIView):
    serializer_class = PostCreateSerializer
    queryset = Post.objects.all()

class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostCreateSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class CreatePostCategoryAPIView(generics.CreateAPIView):
    serializer_class = PostCategoryCreateSerializer
    queryset = PostCategory.objects.all()