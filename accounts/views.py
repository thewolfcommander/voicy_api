from django.contrib.auth.models import User
from rest_framework.views import Response, status
from rest_framework import generics, permissions, authentication

from accounts.permissions import IsOwnerOrReadOnlyProfile, IsOwnerOrReadOnlyUser
from accounts.models import (
    UserProfile,
    UserProfileFollower,
    ChatTransactionApprove
)

from accounts.serializers import *


class RegisterUserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.AllowAny]


class UserProfileCreateAPIView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class ListAllUsersAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.IsAuthenticated]



class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnlyUser]
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)



class ListAllUserProfilesAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileShowSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileShowSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnlyProfile]


    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class FollowerAPIView(generics.CreateAPIView):
    queryset = UserProfileFollower.objects.all()
    serializer_class = UserProfileFollowerSerializer
    permission_classes = [permissions.IsAuthenticated]


class ListFollowerAPIView(generics.ListAPIView):
    queryset = UserProfileFollower.objects.all()
    serializer_class = UserProfileFollowerShowSerializer
    filterset_fields = ['follower_profile', 'follower']
    permission_classes = [permissions.IsAuthenticated]


class UnfollowAPIView(generics.DestroyAPIView):
    queryset = UserProfileFollower.objects.all()
    serializer_class = UserProfileFollowerSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.follower_profile.followers_count -= 1
            instance.follower_profile.save()
            instance.follower.following_count -= 1
            instance.follower.save()
            self.perform_destroy(instance)
        except:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


class ChatTransactionApproveListCreateAPIView(generics.ListCreateAPIView):
    queryset = ChatTransactionApprove.objects.all()
    serializer_class = ChatTransactionApproveSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = [
        'sender',
        'reciever',
        'is_approved',
        'is_rejected'
    ]


class ChatTransactionApproveDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChatTransactionApprove.objects.all()
    serializer_class = ChatTransactionApproveSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)