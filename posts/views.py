from rest_framework import generics, permissions

from accounts.permissions import IsOwnerOrReadOnlyPost
from posts.serializers import *
from posts.models import *


class ListPostAPIView(generics.ListAPIView):
    serializer_class = PostShowSerializer
    queryset = Post.objects.all()
    filterset_fields = ['profile', 'category', 'is_source', 'is_verified',
    'contains_media', 'location_added', 'active']
    permission_classes = [permissions.IsAuthenticated]

class CreatePostAPIView(generics.CreateAPIView):
    serializer_class = PostCreateSerializer
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostCreateSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnlyPost]

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class CreatePostCategoryAPIView(generics.CreateAPIView):
    serializer_class = PostCategoryCreateSerializer
    queryset = PostCategory.objects.all()
    permission_classes = [permissions.IsAuthenticated]